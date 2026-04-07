# Installing your own copy of the QuickView tool family at NERSC 

The steps described below follow the same logic as documented on
[this page](./installation_at_nersc.md),
expect that

- the tools are installed to a different path, `/global/cfs/projectdirs/m4359/tools/`,
  which we refer to as `${pathRoot}` in the following, and
- the environment is named `quickview-env`,
  which we refer to as `${envName}`

## Create a `conda` environment

Create a directory for the conda environment:
```sh
mkdir -p ${pathRoot}/conda-envs
```

Create an environment inside that directory:
```sh
module load conda
conda create --prefix ${pathRoot}/conda-envs/${envName} python=3.13
```

## Activate the environment and install tools in the family

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

At this point, the user should be able to use the following commands to launch the individual tools:

QuickView:
```
quickview -p 0
``` 
QuickCompare:
```
quickcompare -p 0
```
 
## Recommended: executable Shortcuts

Since the conda environment and tools are installed in custom paths, it will
be useful to create shortcuts so that the apps can be lauched using short commands.

### Set up, step 1

We can create a script `${pathRoot}/quickview` with the following content
```sh
#!/usr/bin/env bash

pathRoot="/global/cfs/projectdirs/m4359/tools/"
envName="quickview-env"

module load conda
conda activate ${pathRoot}/conda-envs/${envName} 
quickview -p 0 --fast
```
And to make the shortcut executable, we do
```
chmod +x ${pathRoot}/quickview
```

Similarily, we create a script`${pathRoot}/quickcompare` with the following content
```sh
#!/usr/bin/env bash

pathRoot="/global/cfs/projectdirs/m4359/tools/"
envName="quickview-env"

module load conda
conda activate ${pathRoot}/conda-envs/${envName}
quickcompare -p 0
```
And to make the shortcut executable, we do
```
chmod +x ${pathRoot}/quickcompare
```

### Set up, step 2

In the `.bashrc` or `.cshrc` file in your home directory, add
```
alias quickv='/global/cfs/projectdirs/m4359/tools/quickview'
alias quickc='/global/cfs/projectdirs/m4359/tools/quickcompare'
```
### Using the apps through shortcuts

After the two setup steps have been completed, the user should be able
to launch the tools by symply typing `quickv` or `quickc`
in a terminal window in the JupyterHub.
Again, the same commands can be used regardless of whether the terminal
window is connected to a login node or a shared GPU node etc. 


## Updating an application

In order to update a given application you will need to find the version you want to install and then run something like:

```sh
module load conda
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview

conda install "e3sm-quickview>=1.3.3" # <== fix version
```
