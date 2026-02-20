# Install and Launch for App Developers

At version 1.0, QuickView is expected to be installed and used from a personal
computer with the data files also being local. Future versions will support the
server-client model allowing access to remote data.

Releases so far have focused on macOS. Support for more systems will be added in
the near [future](../future.md).

---

## Clone the repo

```
git clone https://github.com/ayenpure/QuickView.git
cd QuickView
```

---

## Install basic requirements

```
# Set up conda environment
conda env create -f quickview-env.yml
conda activate quickview

# Install QuickView
pip install -e .
```

---

## Launch the app from command line

To launch the EAM QuickView GUI in its dedicated window, use

```
quickview -data /path/to/your/data.nc --con /path/to/connectivity.nc
```

To launch server only (no browser popup), use

```
quickview -df /path/to/your/data.nc -cf /path/to/connectivity.nc --server
```

---

## Development utilities

```
# Run linter
ruff check quickview/

# Run tests
python -m quickview.app --help
```

---

## NERSC setup

First you need to create a conda environment that is shared.

```
mkdir -p /global/common/software/m4359/conda-envs

module load conda
conda create --prefix /global/common/software/m4359/conda-envs/e3sm-quickview python=3.13
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview
conda install e3sm-quickview
```

Then you can create an application shortcut by editing the file
`/global/common/software/m4359/quickview` with the following content

```
#!/usr/bin/env bash

module load conda
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview
quickview -p 0
```

Then you can make it executable
`chmod +x /global/common/software/m4359/quickview`

If you want to update the application, you can run the following

```
module load conda
conda activate /global/common/software/m4359/conda-envs/e3sm-quickview

conda install "e3sm-quickview>=1.3.3" # <--- Update version number
```
