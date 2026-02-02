# QuickView Known Issues

## Issue: Blank Images During Time Slider Update

**Date**: 2026-02-02

**Description**: 
When changing the time slider, blank images appear briefly before the actual data renders. This appears to be a trame redraw state issue during data loading.

**Symptoms**:
- Blank frames flash before the visualization updates
- Occurs when scrubbing through time steps

**Root Cause Analysis**:
The `render()` is called immediately after `UpdatePipeline()`, but the data may not be fully propagated through the VTK pipeline yet. This causes a blank frame before the actual data appears.

The relevant code path in `app.py`:
```python
def _on_slicing_change(self, var, ind_var, **_):
    self.source.UpdateSlicing(var, self.state[ind_var])
    self.source.UpdatePipeline()

    self.view_manager.update_color_range()
    self.view_manager.render()
```

**Potential Fixes**:

1. **Disable rendering during update, then re-enable**:
```python
def _on_slicing_change(self, var, ind_var, **_):
    self.view_manager.disable_render = True  # Prevent intermediate renders
    self.source.UpdateSlicing(var, self.state[ind_var])
    self.source.UpdatePipeline()
    self.view_manager.update_color_range()
    self.view_manager.disable_render = False
    self.view_manager.render()
```

2. **Use `server.network_completion`** to wait for state sync before rendering

3. **Batch state changes** with `with self.state:` context manager

**Status**: Open

---

## Issue: Slow Pipeline Updates Due to Expensive Clipping Operations (RESOLVED)

**Date**: 2026-02-02

**Description**: 
Pipeline updates (e.g., changing time steps) were taking ~8 seconds due to expensive clipping operations in `EAMTransformAndExtract`, even when using full lat/lon range where no clipping was needed.

**Symptoms**:
- Time slider scrubbing took 8-10 seconds per step
- High memory usage during updates
- UI felt unresponsive

**Root Cause Analysis**:
The `EAMTransformAndExtract` filter in `eam_projection.py` performs 5 VTK operations on every pipeline update:
1. `clipL` - Clip left of 180° meridian
2. `clipR` - Clip right of 180° meridian  
3. `transform` - Translate clipR by -360°
4. `append` - Merge clipL + transform
5. `extract` - Box clip to lat/lon range

For a 25M cell dataset, this creates **5-6x data duplication** in memory:

| Step | Data Copy |
|------|-----------|
| Input data | 1x (original) |
| `clipL` output | 1x |
| `clipR` output | 1x |
| `transform` output | 1x |
| `append` output | 1x |
| `extract` output | 1x |

**Worst case: 5-10 GB peak memory** for a 1-2 GB dataset.

**Profiling Results (Before Fix)**:
```
[EAMTransformAndExtract] Input cells: 25,165,824
[EAMTransformAndExtract] clipL: 0.51s
[EAMTransformAndExtract] clipR: 0.51s
[EAMTransformAndExtract] transform: 0.11s
[EAMTransformAndExtract] append: 0.94s
[EAMTransformAndExtract] extract: 3.76s
[EAMTransformAndExtract] Total: 5.83s
[Pipeline.UpdatePipeline] Total: 7.64s
```

**Solution Implemented**:
Added `INITIAL_CLIP_ON` flag and skip logic in `eam_projection.py`:

```python
# Static variable to control clipping
INITIAL_CLIP_ON = True

def _should_skip_clipping(self):
    """Returns True if clipping should be skipped (pass-through mode).
    
    Logic:
    - Full range → always skip (fast, no clipping needed)
    - Cropped range + INITIAL_CLIP_ON=True → perform clipping
    - Cropped range + INITIAL_CLIP_ON=False → skip (disables crop feature)
    """
    # Always skip if using full range (no clipping needed)
    if (self.longrange == [-180.0, 180.0] and 
        self.latrange == [-90.0, 90.0]):
        return True
    # Only skip non-full-range if clipping is globally disabled
    if not INITIAL_CLIP_ON:
        return True
    return False

def RequestData(self, request, inInfo, outInfo):
    # ... 
    if self._should_skip_clipping():
        outData.ShallowCopy(inData)  # Pass-through, no data copy
        return 1
    # ... existing clipping code ...
```

**Profiling Results (After Fix)**:
```
[EAMTransformAndExtract] Input cells: 25,165,824
[EAMTransformAndExtract] SKIPPED (clip disabled or full range)
[EAMTransformAndExtract] Total: 0.00s
[Pipeline.UpdatePipeline] Total: 1.22s
```

**Performance Improvement**:
- Pipeline update: **8s → 1s (8x faster)**
- Memory: No extra copies when at full range
- Cropping still works when user changes lat/lon sliders

**Status**: Resolved

**Files Modified**:
- `src/e3sm_quickview/plugins/eam_projection.py`

---

## Issue: Antimeridian (180° Longitude) Handling is Expensive

**Date**: 2026-02-02

**Description**: 
The `EAMTransformAndExtract` filter performs expensive clipping operations to handle cells that cross the 180° meridian (antimeridian). This is necessary for correct rendering but costly even when most data doesn't cross this boundary.

**The Problem**:
When geographic data spans the 180° meridian, cells/polygons that cross this boundary cause rendering artifacts:

```
        -180°                    0°                    +180°
          |                      |                      |
    ------+----------------------+----------------------+------
          |    ← Data here       |       Data here →   |
          |                      |                      |
          |     Cell crosses 180° line = PROBLEM       |
```

A cell with vertices at longitude 179° and -179° (only 2° apart geographically) would render as spanning 358° instead of wrapping correctly.

**Current Solution**:
The filter handles this by:
1. `clipL` — Keep cells left of 180°
2. `clipR` — Keep cells right of 180°
3. `transform` — Shift right-side cells by -360° (181° → -179°)
4. `append` — Merge both halves

This works but creates 4-5x data copies and takes ~3 seconds even when no cells actually cross the meridian.

**Potential Cheaper Alternatives**:

### 1. Pre-check if meridian handling is needed (Cheapest)
Check data bounds first. If all longitudes are within [-180, 180] and no cells cross 180°, skip the clipL/clipR/transform/append sequence entirely:

```python
bounds = inData.GetBounds()  # [xmin, xmax, ymin, ymax, zmin, zmax]
if bounds[0] >= -180.0 and bounds[1] <= 180.0:
    # No meridian crossing, skip to extract directly
    pass
```

### 2. Point coordinate wrapping (No clipping needed)
Instead of clipping cells, wrap point coordinates in-place:

```python
points = inData.GetPoints()
for i in range(points.GetNumberOfPoints()):
    x, y, z = points.GetPoint(i)
    if x > 180.0:
        points.SetPoint(i, x - 360.0, y, z)
```

This modifies coordinates without creating new cells — much faster for large datasets.

### 3. Use vtkThreshold instead of vtkClip
For the final lat/lon box extraction, `vtkThreshold` on cell centers is faster than `vtkTableBasedClipDataSet` for axis-aligned bounds.

### 4. Handle in the reader (Best long-term)
Wrap coordinates when building geometry in `eam_reader.py`, so downstream filters never see coordinates > 180°.

**Recommendation**: 
Option 1 (pre-check bounds) + Option 2 (coordinate wrapping) would eliminate most cost while handling edge cases correctly.

**Status**: Open (current workaround: skip all clipping at full range)

---

## Issue: GetBounds() Recomputed Every Pipeline Update

**Date**: 2026-02-02

**Description**: 
`GetDataInformation().GetBounds()` is called on every pipeline update, taking ~0.8s to iterate through 25M+ points to compute min/max coordinates — even though geometry never changes between time steps.

**Profiling Evidence**:
```
[AtmosProj.UpdatePipeline] 0.19s
[GetDataInformation.GetBounds] 0.78s   ← 78% of remaining pipeline time
[ContProj.UpdatePipeline] 0.00s
[GridProj.UpdatePipeline] Total: 0.99s
```

**Root Cause**:
In `pipeline.py`, bounds are recomputed every time:

```python
def UpdatePipeline(self, time_value=0.0):
    ...
    atmos_proj.UpdatePipeline(time_value)
    self.moveextents = atmos_proj.GetDataInformation().GetBounds()  # Called every time!
    ...
```

**Why This is Wasteful**:
- `GetBounds()` iterates through **all points** to find min/max X, Y, Z
- Geometry is **constant** — only field values change between time steps
- Result is **always the same** — wasted 0.8s per update

**Solution**:
Cache bounds after first computation:

```python
def UpdatePipeline(self, time_value=0.0):
    ...
    atmos_proj.UpdatePipeline(time_value)
    
    # Cache bounds - geometry doesn't change between time steps
    if not hasattr(self, '_cached_moveextents') or self._cached_moveextents is None:
        self._cached_moveextents = atmos_proj.GetDataInformation().GetBounds()
    self.moveextents = self._cached_moveextents
    ...
```

**Expected Improvement**:
- Pipeline update: **1.0s → 0.2s** (after first load)
- Combined with clipping fix: **8s → 0.2s total (40x faster)**

**Status**: Open

**Files to Modify**:
- `src/e3sm_quickview/pipeline.py`

---
