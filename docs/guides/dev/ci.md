# Continuous integration

QuickView has 4 workflows:
- __website (automatic):__ Update website when code get pushed to the repository.
- __test (automatic):__ Validate PR and code based on the current tests implemented.
- __release (manual):__ Will look at git history to generate version bump with associated changelog. This  will publish a new version to PyPI. Then conda-forge will catchup the new version and will automatically publish it the next day or so.
- __package (automatic):__ Will generate the desktop bundle and link them to the release entry inside Github.

## WebSite

The WebSite is using VitePress to present the various markdown files living under `./docs/**/*.md` into a website available at https://kitware.github.io/QuickView/.

## Release

This workflow needs to be [triggered manually on this page](https://github.com/Kitware/QuickView/actions/workflows/release.yml) by clicking on the __Run workflow__ button.
