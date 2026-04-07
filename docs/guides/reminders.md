## Key reminders for using QuickView and other tools in the family

::: tip Two modes of use
QuickView can be used in two modes:
a ^^new-viz^^ mode (for starting a new visualization) or
a ^^resume^^ mode (for resuming an analysis). Further details can be found on
the [toolbar description page](/guides/quickview/toolbar.md).
:::

::: tip "Connectivity Files"

Since E3SM's horizontal grids are unstructured meshes from ParaView's perspective,
connectivity files are needed in addition to  the simulation data files.
Further details can be found on the documentation pages
describing the [connectivity files](/guides/connectivity.md) and the
[toolbar](/guides/quickview/toolbar.md).
:::

::: tip "The `LOAD VARIABLES` Button"

Most buttons, sliders, and selection boxes in the GUI apply their effects
immediately upon user interaction. The only exception is the variable
selection: After variables are chosen for the first time following file load
or after the selection is changed, the user ^^must^^ click the `LOAD VARIABLES`
button in the [toolbar](/guides/quickview/toolbar.md) for the new selection to take effect.
:::

::: tip "Viewport Layout"

The QuickView app is designed to present multiple variables simultaneously
in an informative way. Users can ^^rearrange^^ the individual views
(i.e., contour plots) in the [viewport](/guides/quickview/viewport.md)
and ^^resize^^ each view.

Furthermore, if a user saves a state file after these
adjustments, they can later resume their analysis with the customized
arrangement.
:::

