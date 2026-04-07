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
- Optional but recommended: in the terminal, use the `cd` command to go to the directory where your data files are located.
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
  A click on the URS will bring up the graphical UI in a brower window.

::: tip Tip: Choosing a server for your analysis session
JupyterHub's control panel allows users to choose from serveral different types of resources
for their computing and analyais needs, including, e.g., login node, shared GPU node,
exclusive nodes, etc. Since login nodes are shared by users and hence can get very busy
or run into memory constraints, we recommend that users choose a shared GPU node
or an exclusive node and user our tools there.

Regardless of which type of node is chosen, the same commands (as listed above)
are used to launch our tools in the QuickView family.
:::

## For NERSC user's who have not used JupyterHub

Please visit [NERSC's Jupyter documentation](https://docs.nersc.gov/services/jupyter/)
to learn how to use the JupyterHub service.

## If you do not yet have any user account at  NERSC

Please visit [this page](https://docs.nersc.gov/accounts/#obtaining-an-account)
to understand how to get started.
