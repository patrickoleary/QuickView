# Simulation Files 

The QuickView family of tools has been developed using history output
on the physics grids (`pg2` grids) of the E3SM Atmosphere Model, EAM,
generated using EAMv2, v3, and intermediate versions towards v4
(EAMxx). Sample output files can be found on
[Zenodo](https://zenodo.org/records/16922607).


## 2D variables

QuickView recognizes variables with—and only with—the **dimensions `time` and
`ncol`** as 2D variables, i.e., physical quantities varying with latitude and
longitude but without a vertical dimension. These are referred to as "surface
variables" in the control panel. For these variables, the only required
^^coordinate variable^^ is ^^`time`^^. Grid information, including latitude and
longitude, are obtained from the connecitivity file.

If an `area` variable with the dimension `ncol` is also present, this variable
is used for calculating the area-weighted horizontal averages displayed in the
viewport. If the `area` variable is not present, then an arithmetic average is
calculated and displayed.

## 3D variables

If a variables has not only `time` and `ncol` but also a vertical dimension,
QuickView expects the dimension to be named **`lev`** for variables defined at
layer midpoints and **`ilev`** for variables defined at layer interfaces.

For variables defined at layer midpoints, in order for the `Slice Selection`
section of the control panel to work properly, the simulation data file needs to
contain a 1D coordinate variable named `lev`, the values of which are
interpreted as pressure in hPa. If `lev` is not present, QuickView attempts to
find two 1D variables, `hyam` and `hybm`, of that dimension size, from which
QuickView calculates `lev` using

```
lev = (hyam * P0) + (hybm * PS0)
```

where PS0 = 1000 hPa; P0 is read from the data file and set to 1000 hPa if not
found.

Similarly, for variables defined at layer interfaces, QuickView looks for either
`ilev` or `hyai` and `hybi` for parsing the vertical dimension.

## Variable with more dimensions

QuickView currently only visualizes the variables types discussed above. For
variables that have extra dimensions in addition to `time`, `ncol`, and `lev` or
`ilev`, for example aggregated tracer arrays or
[COSP](https://climatedataguide.ucar.edu/climate-data/cosp-cloud-feedback-model-intercomparison-project-cfmip-observation-simulator-package)-related
variables, support can be provided if there is sufficient interest from the
users.

## Missing values

If a variable has an attribute named `missing_value` or `_FillValue`, the value
is converted to NaN and ignored in the calculation of global averages and for
the visualization.

