# The QuickView tool family at NERSC

Our tools have been installed at NERSC,
the [National Energy Research Scientific Computing Center](https://www.nersc.gov/)
and are continually updated there.
The following sections on this page contain instructions for users who would like to use our installations.

[[toc]]

User's who would like to understand how our installation was done
or how to have their own installation are referred to [this page](installation_at_nersc.md).

## Quickstart for users familiar with JupyterHub

- Login to [JupytherHub](https://jupyter.nersc.gov/hub/login) and start a terminal window.
- *Optional but recommended*: in the terminal, use the `cd` command to go to the directory
  where your data files are located (or a directory closer to the data files than your home directory).
- QuickView version 2 can be launched using the following command:
```
/global/common/software/m4359/quickview2
```  
- QuickCompare can be launched using the following command:
```
/global/common/software/m4359/quickcompare
```
- After a few seconds, the Terminal window will say "Use URL below to connect to the application:"
  and shows a URL starting with `https://`.
  A click on the URL will bring up the graphical UI in a brower window.

::: tip Tip 1: Choosing a server for your analysis session.
JupyterHub's control panel allows users to choose from serveral different types of resources
for their computing and analyais needs, including, e.g., login node, shared GPU node,
exclusive nodes, as explained in [NERSC's documentation](https://docs.nersc.gov/services/jupyter/reference/).

Since login nodes are shared by users and hence can get very busy or run into memory constraints,
and since our tools can make use of GPUs for interactive rendering.
we recommend that users choose a shared GPU node or an exclusive GPU node.

Keep in mind, though, that time spent on shared GPU nodes or exclusive nodes
will be charged to your project's allocation.
:::

::: tip Tip 2: Same executable for all kinds of nodes.
Regardless of which type of node is chosen, the same commands (as listed above)
are used to launch our tools in the QuickView family.
:::

::: tip Tip 3: No need to manually load `conda`.
When one of the commands provided above is used to lunch tools in the QuickView family,
there is no need to manually load `conda` or the conda environment that our tools are installed in.
This is because the above-mentioned commands are in fact scripts that have included those steps.
:::

::: warning Reminder: Shut down the server when you are done.
After finishing your analysis, please remember to shut down the connection to your selected
server (node) to stop the charging of ours to your project's allocation. 
This is explained at the end of
[this video](https://docs.nersc.gov/beginner-guide/#keypad-entry-log-in-using-jupyter),
and here is a recap of the steps (clicks):
- go to the JupytherHub window/tab in your browser,
- click `File`,
- scroll down and choose `Hub Control Panel`,
- in the Control Panel that brought up in a new brower tab/window, click on the red "stop" button
  for the server to shut down. An example is shown in the screenshot below.

![JupyterHub_control_panel_with_stop_button.png](/nersc/JupyterHub_control_panel_with_stop_button.png)
:::

## For NERSC user's who have not used JupyterHub

Please see this section of
[NERSC's documentation](https://docs.nersc.gov/beginner-guide/#keypad-entry-log-in-using-jupyter),
especially the video "How to log in to Perlmutter with Jupyter",
to learn how to use the service.

## If you do not yet have any user account at  NERSC

Information on [this page](https://docs.nersc.gov/accounts/#obtaining-an-account)
can help get you started.
