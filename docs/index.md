---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "The QuickView Family"
  text: "for Earth System Models"
  tagline:
    Quick, intuitive, and interative exploration of simulation data.
  image: /banner.png
  actions:
    - theme: alt
      text: Installation
      link: /guides/installation
    - theme: brand 
      text: Getting Started 
      link: /guides/data
    - theme: brand 
      text: Running at NERSC
      link: /nersc/

features:
  - icon:
      src: /logos/E3SM_Logo.png
      width: 120px
      title: Purpose
    details:
      Currently supported are simulation output from   
      the Exascale Earth System Model (E3SM) model
      on cubed-sphere "physics" grids.
  - icon:
      src: /logos/ParaView_Mark.png
      width: 60px
      title: Engine and UI 
    details:
      Python- and Trame-based User Interfaces (UI) provide
      intuitive access to ParaView's powerful analysis and visualization
      capabilities but without requiring a steep learning curve.
  - icon:
      src: /logos/nersc.png
      width: 170px
      title: Remote Data 
    details:
      The tools have been deployed at NERSC so that users can
      directly access simulation data there.
      No installation is required on the user's end,
      as the UI shows up in a brower window.
  - icon:
      src: /logos/SciDAC-logo.png
      width: 140px
      title: Funding Source 
    details:
      The development of this tool suite is supported by the
      U.S. Department of Energy's SciDAC program.
---
