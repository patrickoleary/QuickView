![toolbar](../../images/toolbar.png)

## Resume mode: pick up where you left off

![state save and load](../../images/toolbar_state_save_and_load.png){
width="10%", align=right }

The current state of the visualization can be saved—and reloaded later to resume
the analysis—using the `Save State` (downward arrow) and `Load State` (upward
arrow) buttons shown here.

For loading a state, the upward arrow button brings up a window for the user to
select a state file from the computer. After the file is selected and the `Open`
button in that dialogue window is clicked, the app will immediately start
loading the state; the user is _not_ supposed to click on the Load Files button
designed for the new-viz scenario. If the state file is successfully loaded (the
contents are correctly parsed), the red circle-and-exclamation icon will turn
into to a green circle-and-check-mark icon, like in the new-viz mode. Loading a
state for an ne30 simulation usually takes a couple of seconds.


---

## Other elements of the toolbar

![hamburger icon](../../images/toolbar_hamburger.png){ width="6%", align=right }

**Control Panel Hide/Show**: The hamburger icon (three stacked lines) at the
left end of the toolbar hides or shows the [control panel](control_panel.md).

![busy indicator](../../images/toolbar_busy_indicator.png){ width="5%",
align=right }

**Busy Indicator**: The gray circle is a busy indicator. When a rotating segment
appears, the app is processing data in the background—for example, loading data
files or a state file as explained earlier on this page, or loading newly
selected variables (see description of the [control panel](control_panel.md)).

![LOAD VARIABLES button](../../images/toolbar_load_variables.png){ width="18%",
align=right }

**`LOAD VARIABLES`**: The `LOAD VARIABLES` button, when clicked, executes the
action of loading the [user-selected variables](control_panel.md) from the data
file and displaying them in the [viewport](viewport.md).

![colormap groups](../../images/toolbar_colormap_groups.png){ width="12%",
align=right }

**Colormap Groups**: The eye icon is a toggle for loading a group of
colorblind-friendly colormaps to the GUI for the user to choose from in the
[viewport](viewport.md); A lot of these colormaps are from
[Crameri, F. (2018)](https://doi.org/10.5281/zenodo.1243862). The paint palette
icon is a toggle for loading a set of colormaps that may not be
colorblind-friendly; Currently, these are "presets" from
[PareView](https://www.paraview.org/).

![camera actions](../../images/toolbar_camera_actions.png){ width="25%",
align=right }

