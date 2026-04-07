# QuickCompare @ NERSC

## Log in to NERSC

To use QuickCompare at NERSC to directly access and analyze data files there,
users need to first connect to NERSC using JupyterHub, as described
[on this page](./jupyter_at_nersc.md).

Once connected,

- Start a Terminal from the Launcher options of JupyterHub.
  You will likely need to scroll down in the Launcher in order to
  see the "Other" section and the Terminal icon there, as shown in the screenshot below.
  Click on the Terminal icon, and the Launcher window should turn into a shell.
  !["Other" section of JupyterHub Launcher window](./jupyter_launcher_terminal.png)

- *Optional but recommended*: in the shell, use the `cd` command to go to
  the directory where your data files are located (or a directory closer to the data files than your home directory).
  While that step is optional, it may save you quite some clicks later in the graphical UI.

- Starting QuickCompare using the command `/global/common/software/m4359/quickcompare` in the shell.

- After a few seconds, the Terminal window will provide a URL, similar to the screenshot below.
  A click on the URL will bring up the graphical UI in a separate brower window or tab.
  <!-- ![](./quickview/quickview-terminal-with-url.png) -->

:::danger FIXME - image
:::

- The graphical UI will prompt you to choose connectivity and simulation files, see example below.
  Double click your connecitivity file and then the simulation files, then
  click on the blue "Load Files" button in the bottom-right corner
  <!-- ![](./quickview/quickview-file-loading.png) -->

:::danger FIXME - image
:::

- **Need to talk about two-sim or multi-sim comparisons** 

:::danger FIXME - image
:::

- Finally, select the variables you want to load and inspect.
  <!-- ![](./quickview/quickview-variable-selection.png) -->

## Shut down the server when you are done

::: warning IMPORTANT: Shut down the server when you are done.
After finishing your analysis, please remember to shut down the connection to your selected
server (node) to stop the charging of hours to your project's allocation.
This is explained at the end of
[this video](https://docs.nersc.gov/beginner-guide/#keypad-entry-log-in-using-jupyter),
and below is a recap of the steps (clicks):
- go to the JupytherHub window/tab in your browser,
- click `File` in the top-left corner,
- scroll down and choose `Hub Control Panel`,
- in the Control Panel brought up in a new browser tab/window, click on the red "stop" button
  for the server to be shut down. An example is shown in the screenshot below.

![](./login/login-04.png)
:::
