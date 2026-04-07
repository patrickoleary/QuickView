---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "The QuickView Family"
  text: "Intuitive Analysis Tools for Earth System Models"
  tagline:
    Get started with the QuickView family of tools to quickly explore and compare
    your simulation output from Earth system models.
  image: /banner.png
  actions:
    - theme: alt
      text: Installation
      link: /guides/installation
    - theme: alt
      text: Getting started
      link: /guides/data
    - theme: brand
      text: Running at NERSC
      link: /nersc/

features:
  - icon:
      src: /logos/E3SM_Logo.png.png
      width: 120px
      title: Purpose
    details:
      The QuickView family is a collection of open-source, interactive
      visualization tools designed
      for scientists working with the Exascale Earth System Model (E3SM).
  - icon:
      src: /logos/ParaView_Mark.png
      width: 60px
      title: Engine and UI 
    details:
      The Python- and Trame-based User Interface (UI) provides
      intuitive access to ParaView's powerful analysis and visualization
      capabilities but without requiring a steep learning curve.
  - icon:
      src: /logos/nersc.png
      width: 170px
      title: Remote Data 
    details:
      Tools in this family have been deployed at NERSC so that users can
      directly access simulation data there.
      No installation is required on the user's end, as the UI shows up in
      a brower window.
  - icon:
      src: /logos/SciDAC-logo.png
      width: 140px
      title: Funding Source 
    details:
      The development of this tool suite is an ongoing interdisciplinary collaboration
      supported by the U.S. Department of Energy Office of Science’s Advanced
      Scientific Computing Research (ASCR) and Biological and Environmental
      Research (BER) via the Scientific Discovery through Advanced Computing
      (SciDAC) program.
  - icon:
      src: /logos/Kitware.png
      width: 140px
      title: Collaborators 
    details:
      The tool family is collaboratively designed by
      Earth system scientists at Pacific Northwest National Laboratory
      and visual analytics specialists at Kitware Inc. 
---
