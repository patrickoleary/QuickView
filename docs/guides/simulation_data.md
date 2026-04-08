# Simulation Files 

The QuickView family of tools has been developed using history output
on the physics grids (`pg2` grids) of the E3SM Atmosphere Model, EAM,
generated using EAMv2, v3, and intermediate versions towards v4
(EAMxx). Some sample output files can be found on
[Zenodo](https://zenodo.org/records/16922607).

## The horizontal dimension 

Starting from version 2, the ParaView Reader used in the tools
has been generalized to handle all NetCDF
variables on `ne*pg2` cubed-sphere meshes regardless of what name is used
for the horizontal dimension (e.g., `ncol` in EAM files or
`lndgrid` in ELM files). 

Furthermore, QuickView2 has been generalized to visualize all variables
in a NetCDF file that have a horizontal dimension matching the connecitivity file,
regardless of how many additional dimensions the variables have.


## Global averages

If an `area` variable with the correct horizontal dimension is present
in the simulation file, this variable
is used for calculating the area-weighted horizontal averages displayed in the
viewport. If the `area` variable is not present, then an arithmetic average is
calculated and displayed.

## Missing values

If a variable has an attribute named `missing_value` or `_FillValue`, the value
is converted to NaN and ignored in the calculation of global averages and for
the visualization.

## File groups

:::danger FIXME - add contents
::: 
