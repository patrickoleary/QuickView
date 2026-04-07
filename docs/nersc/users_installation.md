# Installing your own copy of the QuickView tool family at NERSC 

The steps described below follow the same logic as documented on
[this page](./public_installation.md),
expect that

- the tools are installed to a different path, `/global/cfs/projectdirs/m4359/tools/`,
  which we refer to as `${pathRoot}` in the following, and
- the conda environment is named `quickview-env`,
  which we refer to as `${envName}` below.

::: warning Note!
Please **use a login node for the installation**. After that,
the tools can be used on login nodes or other types of nodes
via the same commands/shortcuts.
:::

## Create a `conda` environment

Create a directory for the conda environment needed for installing our tools:
```sh
mkdir -p ${pathRoot}/conda-envs
```

Create an environment inside that directory:
```sh
module load conda
conda create --prefix ${pathRoot}/conda-envs/${envName} python=3.13
```

## Activate the environment and install our tools

Install QuickView
```sh
conda activate ${pathRoot}/conda-envs/${envName}
conda install conda-forge::e3sm-quickview
```
In the same environment, also install QuickCompare:
```sh
conda install conda-forge::e3sm_compareview
```

## Using the installed apps

At this point, the user should be able to use the following commands to launch
the individual tools, assuming the conda environment has been activated.
(But read the [next section](#recommended:-executable-shortcuts) if you expect to use the tools often.)

QuickView:
```
quickview -p 0
``` 
QuickCompare:
```
quickcompare -p 0
```
 
## Recommended: executable shortcuts

Since the conda environment and tools are installed in custom paths, it will
be useful to create shortcuts so that the apps can be lauched using very short 1-line commands.

### Setup step 1

We can create a script `${pathRoot}/quickview2` with the following contents:
```sh
#!/usr/bin/env bash

pathRoot="/global/cfs/projectdirs/m4359/tools/"
envName="quickview-env"

module load conda
conda activate ${pathRoot}/conda-envs/${envName} 
quickview -p 0
```
And to make the shortcut executable, we do
```sh
chmod +x ${pathRoot}/quickview2
```

Similarily, we create a script`${pathRoot}/quickcompare` with the following contents:
```sh
#!/usr/bin/env bash

pathRoot="/global/cfs/projectdirs/m4359/tools/"
envName="quickview-env"

module load conda
conda activate ${pathRoot}/conda-envs/${envName}
quickcompare -p 0
```
And to make the shortcut executable, we do
```sh
chmod +x ${pathRoot}/quickcompare
```

### Setup step 2

In the `.bashrc` or `.cshrc` file in your home directory, add something like
```sh
alias quickv='/global/cfs/projectdirs/m4359/tools/quickview2'
alias quickc='/global/cfs/projectdirs/m4359/tools/quickcompare'
```
### Using the apps through shortcuts

After the two setup steps have been completed, the user should be able
to launch the tools by simply typing `quickv` or `quickc`
in a terminal window in the JupyterHub.
Again, the same commands can be used regardless of whether the terminal
window is connected to a login node or a shared GPU node etc. 


## Updating an application

In order to update the tools to the newest available versions on conda-forge
(see links in the summary table on [this page](/guides/install_and_launch.md),
you will need to find the versions you want to install and then run something like
the following.

```sh
pathRoot="/global/cfs/projectdirs/m4359/tools/"
envName="quickview-env"

quickview_version_new="2.1.1"
quickcomp_version_new="1.3.4"

module load conda
conda activate ${pathRoot}/conda-envs/${envName}

conda install   "e3sm-quickview>=${quickview_version_new}"
conda install "e3sm_compareview>=${quickcomp_version_new}"
```
