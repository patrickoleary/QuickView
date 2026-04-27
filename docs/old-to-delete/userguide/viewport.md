# Viewport

Once the user has selected variables using the [control panel](control_panel.md)
and clicked the `LOAD VARIABLES` button in the toolbar, the app
will show each variable in its own little frame (which we refer to as a "view")
inside the viewport. On the right is an example showing four views.

Within each view, the variable name is noted together with the indices of the
vertical level (if applicable) and time slice being displayed, and the
area-weighted global average on that vertical level. If the "area" variable is
not present in the data file, then the arithmetic average is calculated and
displayed.

---

## Custimizing the viewport


To help present multiple variables in an informative way, the app allows users
to

- rearrange the views via ^^drag-and-drop^^, and
- resize each view separately by clicking and dragging its ^^bottom-right
  corner^^.

The screenshot on the right shows an example with rearranged views.

Furthermore, if a user saves a state file after these adjustments, they can
later continue their analysis with the customized layout by using the app in the
resume mode, as described in on the description of the toolbar.

---

## Custimizing individual views


!!! tip "Tip: Automatic or Fixed Colormap Ranges"

    If the user specifies maximum and/or minimum values in the mini menu, a blue icon
    with a picture of a lock and the text "Manual" will appear above the maximum
    value, as can be seen on the right in the example shown above.
    In such a case, when the "play" button in the [control panel](control_panel.md)
    is used to cycle through different data slices,
    the colormap will be fixed to the user-specified range.

