# Development setup

For Python development while you can use a mix of conda and pip install, it is generally not recommended. So we will provide 2 setups and it will be up to the user to choose what better match his usage.

## Conda setup

```sh
# Grab the code you aim to work with
git clone <repository-url>
cd <repository-name>

# Set up conda environment
conda env create -f quickview-env.yml
conda activate quickview

# Install QuickView
pip install -e .
```

Then to run the application

```sh
quickview # or the name of the executable your application is providing
```

## UV setup + Downloaded ParaView

```
# Grab the code you aim to work with
git clone <repository-url>
cd <repository-name>

# Setup your python environment
uv venv -p 3.12 # force python version to match ParaView 6
uv sync --all-extras --dev

# Activate environment
source .venv/bin/activate

# Install commit analysis
pre-commit install
pre-commit install --hook-type commit-msg

# Allow live code edit
uv pip install -e .
```

Then to run the application, you will need ParaView. The example below provide an example for macOS.

```sh
/Applications/ParaView-6.0.1.app/Contents/bin/pvpython --venv .venv -m e3sm_quickview.app
```

With this setup, any commit will be automatically checked with the pre-commit hooks. But you can also run those manually via the command line below:

```sh
pre-commit run --all-files
```
