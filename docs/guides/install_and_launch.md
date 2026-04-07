# Installation

All tools of the **QuickView** family are available as
**conda** packages as well as **pre-compiled desktop bundles**
for various OS's like Mac, Windows, and Linux.
The table below summarizes where the different packages
and bundles can be found.

| Tool name    | Desktop bundle | conda package name | Conda  | PyPI  |
| ------------ | -------------- | ------------------ | ------ | ----- |
| QuickView    | [Download page](https://github.com/Kitware/QuickView/releases) | e3sm-quickview   | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/e3sm-quickview.svg)](https://anaconda.org/conda-forge/e3sm-quickview)     | [![PyPI](https://img.shields.io/pypi/v/e3sm-quickview?label=pypi%20package)](https://pypi.org/project/e3sm-quickview/)      |
| QuickCompare | [Download page](https://github.com/Kitware/E3SMQuickCompare/releases) | e3sm_compareview | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/e3sm_compareview.svg)](https://anaconda.org/conda-forge/e3sm_compareview) | [![PyPI](https://img.shields.io/pypi/v/e3sm-compareview?label=pypi%20package)](https://pypi.org/project/e3sm-compareview/)  |

## Desktop bundles

To deliver pre-compiled standalone desktop applications,
we use [PyInstaller](https://pyinstaller.org/en/stable/) and [Tauri](https://tauri.app/)
to bundle each of our Python-based tools and their dependencies
into a standalone graphical application.
The creation of such a bundle is done by triggering a release using GitHub Actions. 
Hence, the bundles are available from the corresponding GitHub repo's Releases page.
The links are given in the summary table above.

:::danger ATTENTION Mac Users!!
The binaries compiled for Macs have not been signed using an Apple Developer ID.
Hence, after downloading a binary for Mac, the user needs to use the following
command to remove quarantine on the binary.

```
xattr -d com.apple.quarantine <your_filename>.dmg
```

Also note that the **first execution of the app will take a while** as macOS
will check and validate the full application file tree.
:::

## Conda installation

As our tools depend on [ParaView](https://www.paraview.org/) and
require specific features in [Python](https://www.python.org/),
we use conda to facilitate the setup.

For example, to create a conda environment named `quickview-env`
then install QuickView and QuickCompare, we can use the following commands:

```sh
conda create --name quickview-env python=3.13
conda activate quickview-env
conda install conda-forge::e3sm-quickview
conda install conda-forge::e3sm_compareview
```

## Updating conda installation

To update the tools to newer versions, first find the most recent version
numbers using the links in the summary table near the top of this page,
then use the following commands, replacing the version numbers by yours:

```sh
conda activate quickview-env
conda install "e3sm-quickview>=2.1.1"
conda install "e3sm_compareview>=1.3.4"
```

## Using the tools installed via conda

To use the tools installed via conda, open a Terminal window and
activate the conda environment using

```
 conda activate quickview-env
```

Then, in the same window, use one of the following depending on
which tool you'd like to use

```
quickview -p 0
```

```
quickcompare -p 0
```

After some seconds, the Terminal window should indicate that the app has
loaded various plugins and give an URL similar to `http://localhost:50329/`.
**Enter the URL into a web brower** to access the graphical UL.

 
:::tip Tip: First execution on macOS
On macOS, the first execution after installation via conda will also take a while
(e.g., a minute or more),
as the system will validate each Python file for security. But any following
execution should be very quick (a few seconds).
:::
