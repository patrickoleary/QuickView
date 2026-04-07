# NERSC setup explained

Since the QuickView applications are just Python packages, we install them inside conda environment related to their funding project (`/global/common/software/m4359/`).

## Custom conda environments

Create a directory for all the conda environments we aim to enable for our users.

```sh
mkdir -p /global/common/software/m4359/conda-envs
```

Then for each project we will create an environment inside that directory.

```sh
module load conda
conda create --prefix /global/common/software/m4359/conda-envs/e3sm-quickview python=3.13
```

After that you can activate such environment and install the application like QuickView

```sh
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview
conda install e3sm-quickview
```

## Executable Shortcut

Inside `/global/common/software/m4359/` you can create shell script that will provide a shortcut for starting each application.

For example, we've created `/global/common/software/m4359/quickview` with the following content

```sh
#!/usr/bin/env bash

module load conda
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview
quickview -p 0
```

And to make that file executable, you can run `chmod +x /global/common/software/m4359/quickview` to streamline its usage.

## Updating an application

In order to update a given application you will need to find the version you want to install and then run something like:

```sh
module load conda
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview

conda install "e3sm-quickview>=1.3.3" # <== fix version
```
