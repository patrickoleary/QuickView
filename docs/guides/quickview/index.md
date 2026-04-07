# What is QuickView?

**QuickView** is an open-source, interactive visualization tool designed for
scientists working with the
[Energy Exascale Earth System Model (E3SM)](https://e3sm.org/),
with an initial focus on the horizontal meshes used by the atmosphere component, EAM.
QuickView's Python- and
[trame](https://www.kitware.com/trame/)-based User Interface (UI)
provides intuitive access to [ParaView](https://www.paraview.org/)'s powerful
analysis and visualization capabilities without requiring a steep learning curve.

## Quick Start

- [Install and launch](../instal_and_launch) the app.
- Download [connectivity files](https://doi.org/10.5281/zenodo.16908566) of
  EAM's cubed-sphere grids from Zenodo.
- Optional: download
  [sample simulation output](https://zenodo.org/records/16922607) to test the
  app.

For more details, go to the navigation bar of this website and look for our
User's Guide.

## Why QuickView?

While comprehensive visualization tools like
[ParaView](https://www.paraview.org/) and
[VisIt](https://visit-dav.github.io/visit-website/index.html) are widely used in
the scientific community, they often present a steep learning curve—requiring
users who are not experts in visual analytics to navigate unfamiliar interfaces,
functions, and jargon. Moreover, these general-purpose tools may lack
out-of-the-box support for key requirements in atmospheric sciences, such as
globe and map projections or support for specific data formats and structures,
leading to time-consuming customization or feature requests. QuickView was
developed to address these limitations by offering a focused, user-friendly
platform that streamlines the analysis of atmospheric simulations. It minimizes
the need for E3SM developers and users to write custom scripts, thereby
shortening the path from data to insight.

The core goal of QuickView is a first glance at the contents in a simulation
data file, i.e., a first inspection of the characteristic values of physical
quantities and their variations with respect to geographical location, altitude,
and time, as well as a quick inspection across different physical quantities for
similarities or distinctions. Compared to earlier and widely used tools like
[ncview](https://cirrus.ucsd.edu/ncview/) and
[ncvis](https://github.com/SEATStandards/ncvis), QuickView has an emphasis on
multivariate visualization and is currently focused on E3SM.

## Key Features

- Intuitive, minimalist interface tailored for atmospheric modeling.
- Multi-variable visualization with drag-and-drop layout.
- Persistent sessions - pick up where you left off.
- Support for EAM v2, v3, and upcoming v4 output formats.

## Bug reports and feature requests

Please use the
[Issues tab on GitHub](https://github.com/Kitware/QuickView/issues).

## Project Background

The lead developer of QuickView version 2 is
[Sebastien Jourdain (sebastien.jourdain@kitware.com)](https://www.kitware.com/sebastien-jourdain/)
at [Kitware](https://www.kitware.com/). Other key contributors at Kitware
include Berk Geveci, Dan Lipsa, and Will Dunklin.
Key contributors on the atmospheric science side are Hui Wan and Kai Zhang at
[Pacific Northwest National Laboratory](https://www.pnnl.gov/atmospheric-climate-and-earth-sciences-division).

QuickView is a product of an interdisciplinary collaboration supported by
the U.S. Department of Energy Office of Science’s
[Advanced Scientific Computing Research (ASCR)](https://www.energy.gov/science/ascr/advanced-scientific-computing-research)
and
[Biological and Environmental Research (BER)](https://www.energy.gov/science/ber/biological-and-environmental-research)
via the
[Scientific Discovery through Advanced Computing (SciDAC](https://www.scidac.gov/))
program.
