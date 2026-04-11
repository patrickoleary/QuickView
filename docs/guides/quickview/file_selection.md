# Selecting Files for Analysis

QuickView can be used in two modes:
- a **new-viz mode** for starting a new visualization or
- a **resume mode** for continuing an earlier analysis saved in a state file.

## New-viz mode: starting a new visualization

![File loading window](./screenshots/file-upload-outline.png){ width="5%", align=right }

When QuickView is launched using a shell command or the desktop bundle,
or when the user clicks the "File loading" icon on the toolbar,
a dialogue window like the screenshot below will be brought up.
The user is expected to select a connecitivy file and at least one a simulation data file
from the file system.

![File loading window](./screenshots/file_loading_dialogue.png){ width="95%", align=center }

User can single-click a file name and then click the "simulation" or "connectivity"
button in the bottom-left corner to clarify file type,
and repeat these two clicks to have both files specified.

Alternatively, if a filename starts with "connecitivity", then
the user can **double-click** the file to have it automatically recognized as a connectivity file.
Double-clicking a filename not starting with "connectivity" will
have it treated as a simulation file.

After both connectivity and simulation files are selected,
the `Load Files` button in the bottom-right corner will light up.
A single click will start file loading.

If the files are loaded correctly, the UI will change into a layout like
the example below, with the [Variable Selection control panel](./variable_selection)
on the **left** showing a **list of parsed variables** in the simulation file(s)
and the viewport on the **right** showing a **brief introduction to QuickView**.
The user can now start to search for and load variables to inspect.

![File loaded](./screenshots/file_loaded.png){ width="95%", align=center }

::: tip Tip: Loading a file series from the same simulation 
:::

## Resume mode: picking up where you left off

::: danger TO-DO: check and explain state file download and upload
:::

::: info Info: What's in a State File?
A state file is a JSON file that contains the paths and names of
the connectivity and data files being used as well as the settings
the user has chosen for the visualization; the *contents* of the
connectivity and simulation files are *not* included.

If a state file is shared among multiple users or used across different
file systems, or if a user wants to apply the same visualization settings
to a different simulation data file, then the file names and paths
at the beginning of the state file need to be edited before the state
file is loaded in the app.
:::

::: warning Tip: State File Loading Error
If the app seems nonresponsive after a state file has been chosen
and the `Open` button in the dialogue window has been clicked,
there is a high chance that the paths and names of
the connectivity and simulation data files contain errors.
The user should consider using a text editor to inspect the first
few lines of the state file and verify correctness.
:::

