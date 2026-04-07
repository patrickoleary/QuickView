# Key reminders for using QuickView and other tools in the family

::: warning Two modes of use
QuickView can be used in two modes:
a *new-viz* mode (for starting a new visualization) or
a *resume* mode (for resuming an analysis). Further details can be found on
the [toolbar description page](/guides/quickview/toolbar.md).
:::

::: info Connectivity files
Since E3SM's horizontal grids are unstructured meshes from ParaView's perspective,
connectivity files are needed in addition to  the simulation data files.
Further details can be found on the documentation pages
describing the [connectivity files](/guides/connectivity.md) and the
[toolbar](/guides/quickview/toolbar.md).
:::

::: tip Consistency between connecitivity and simulation files
One of the often encountered causes of error when loading files in QuickView is
that the grid described by the connecitivity file does not match the grid in the
simulation data file. Please double check when you run into a loading error.
:::

::: warning The `LOAD VARIABLES` Button
Most buttons, sliders, and selection boxes in the UI apply their effects
immediately upon user interaction. The only exception is variable
selection: After variables are chosen for the first time following file load
or after the selection is changed, the user **must** click the `LOAD VARIABLES`
button at the top of the "Select Variables" control panel for the new selection to take effect.
:::

::: info Show/hide control panels
Most of the buttons in the vertical [toolbar](/guides/quickview/toolbar.md)
are toggles for showing or hiding the corresponding control panels.
These toggles have 1-key shortcuts--see cheat sheet [here](/guides/quickview/shortcuts.md).
Detailed descriptions of the control panels can be found on
[this page](/guides/quickview/control_panels.md).
:::

::: tip Viewport Layout
QuickView is designed to present multiple variables simultaneously
in an informative way. Users can *rearrange* the individual views
(i.e., contour plots) in the [viewport](/guides/quickview/viewport.md)
and *resize* them.

Furthermore, if a user saves a state file after these
adjustments, they can later resume their analysis with the customized
arrangement.
:::
