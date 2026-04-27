# Miscellaneous Features 

This page summarizes several addtional convenient features in QuickView.

## Choosing map projection and extent

The map projection used for the contour plots can be changed using the mini menu
activated by a click on the Earth icon in the vertical tool bar—or by using keyboard shortcuts:

![map projections](./screenshots/map_projections.png){ width="22%", align=right }

- `C` for cylindrical equidistant,
- `R` for Robinson, and
- `M` for Mollweide.


![lat/lon sliders](./screenshots/latlon_sliders.png){ width="70%", align=right }

The map extent, i.e., the latitude-longitude bounds to be displayed in the contour plots,
can be adjusted using the sliders in the lat/lon cropping panel activated by a click on
the Earth grid icon in the vertical toolbar.


## Saving the visualization

In addition to [saving the state](/guides/quickview/file_selection#state-files)
of the current session so that the analysis can be resumed later,
QuickView provides three ways for the user to save the visualization as images
or animations for presentations and manuscripts, etc.:

![image download](./screenshots/image_download.png){ width="20%", align=right }

- A click on the **camera icon** at the end of the vertical **toolbar** saves the entire
  viewport—in its current layout—to the local computer as `FullPanel.png`.

- A click on the **camera icon** next to the variable name **inside a view panel**
  saves that single view as a `.png` file. The file name starts with the variable name;
  dimension names and indices are appended when relevant.


![animation download](./screenshots/animation_download.png){ width="70%", align=right }

- When the animation control panel is expanded, a click on the icon on the right end
  (a downward arrow with two lines) brings up a drop-down menu.
  The user can choose `Full grid` and/or individual variables,
  then click `Export animation`.

Note: as of version 2.5.1, the animation export functionality downloads a folder
of images to the local computer, and the user needs to use a tool to combine
the images into an animation. Direct download of animation files will be provided
soon. 
