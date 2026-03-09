---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "E3SM QuickView"
  text: "Tools for climate data"
  tagline:
    Get started with the QuickView suite of tools to better explore and compare
    your climate data.
  image: /banner.png
  actions:
    - theme: brand
      text: Running at NERSC
      link: /nersc/
    - theme: alt
      text: Getting started
      link: /guides/data
    - theme: alt
      text: Installation
      link: /guides/installation

features:
  - icon:
      src: /logos/opensource.svg
      width: 60px
    # title: OpenSource
    details:
      E3SM QuickView is an open-source, interactive visualization tool designed
      for scientists working with the atmospheric component of the Energy
      Exascale Earth System Model (E3SM), known as the E3SM Atmosphere Model
      (EAM). Its Python- and Trame-based Graphical User Interface (GUI) provides
      intuitive access to ParaView's powerful analysis and visualization
      capabilities, without the steep learning curve.
  - icon:
      src: /logos/nersc.png
      width: 170px
    # title: NERSC
    details:
      The applications from the QuickView suite are installed at NERSC so you
      can just login and use them directly. They are available from within the
      JupyterHub terminal so you can start one or more instance from your
      reserved node. When running them, they will provide you with a URL that
      you can click to enable a full screen experience within your browser while
      allowing multi-screen usage.
  - icon:
      src: /logos/pnnl.svg
      width: 140px
    # title: Collarative research
    details:
      E3SM QuickView is a product of an interdisciplinary collaboration
      supported by the U.S. Department of Energy Office of Science’s Advanced
      Scientific Computing Research (ASCR) and Biological and Environmental
      Research (BER) via the Scientific Discovery through Advanced Computing
      (SciDAC) program. The project is lead by Hui Wan and Kai Zhang at Pacific
      Northwest National Laboratory.
---
