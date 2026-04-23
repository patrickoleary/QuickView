# The QuickView Family

The QuickView family is a collection of tools for interactive
visualization and analysis of Earth system simulation data.
Compared to standardized and formalized diagnostic packages
that produce hundreds of static figures for comprehensive and
in-depth analysis of model evaluation, the focus of the QuickView
family is on interactive explorations that often happen
during the initial stage of an investigation aimed at
reletionship search or code debugging using
simulation output on the model's native grid.

Each tool in the family focuses only on a small set of actions
that we believe are frequently taken by Earth system model
developers and users, allowing the graphical user interface
to stay simple and intuitive.
On the other hand, we are continually summarizing typical analysis
workflows and assessing new needs to add members to the family.

The first two members in the family are
- [QuickView](/guides/quickview/index)
  for simultaneously presenting 2D contour plots of
  multiple physical quantities (variables) in the form of
  global or regional maps, and
- [QuickCompare](/guides/quickcompare/index)
  for contrasting two or more simulations, also using 2D contour plots.

In terms of the computational mesh over the globe,
the tools currently supports only the E3SM Atmosphere Model's
cubed-sphere `ne*pg2` grids, but extensions to other grids are possible.
