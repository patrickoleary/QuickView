# Installation

The application that belong to the **Quick View** suite are available as
**conda** package and standalone desktop application across OS like Mac, Windows
and Linux.

| Applications | conda package    | Releases                                                         | Versions                                                                                                                            |
| ------------ | ---------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| QuickView    | e3sm-quickview   | [Download](https://github.com/Kitware/QuickView/releases)        | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/e3sm-quickview.svg)](https://anaconda.org/conda-forge/e3sm-quickview) |
| QuickCompare | e3sm-compareview | [Download](https://github.com/Kitware/E3SMQuickCompare/releases) | ![PyPI](https://img.shields.io/pypi/v/e3sm-compareview?label=pypi%20package)                                                        |

## Desktop bundle

For standalone application delivery we rely on PyInstaller and Tauri to bundle
our Python applications into a standalone graphical application.

The Continuous integration does the building and bundling of those, therefore,
you will need to download such application from the release page on Github.

:::danger macOS requirement On macOS you will need to unquarantine the binary as
we are not signing it. To do so, you will need to run in your terminal the
following line.

```
xattr -d com.apple.quarantine <your_filename>.dmg
```

Then the **first execution will take a while** as macOS check and validate the
full application file tree.
:::

## Conda installation

As our application depend on ParaView and Python we rely on conda to deliver a
easy to use setup.

```sh
conda create --name quickview-env python=3.13
conda activate quickview-env
conda install e3sm-quickview # replace with application name
```

:::warning macOS specificity On macOS, the first execution will also take a
while as the system validate each python file for security. But any following
execution should be very quick.
:::
