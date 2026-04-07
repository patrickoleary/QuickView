import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/QuickView",
  title: "E3SM QuickView",
  description:
    "How to start with the E3SM QuickView suite to look at your simulation data",
  head: [["link", { rel: "stylesheet", href: "/custom.css" }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    search: {
      provider: "local",
    },
    logo: "/icon-full.png",
    nav: [
      { text: "Home", link: "/" },
      { text: "News", link: "/news" },
      { text: "Gallery", link: "/gallery/" },
      { text: "User's Guide", link: "/guides/reminders" },
      { text: "At NERSC", link: "/nersc/index" },
      { text: "Repo", link: "https://github.com/Kitware/QuickView" },
      { text: "Bugs and Requests", link: "https://github.com/Kitware/QuickView/issues" },
    ],

    sidebar: {
      "/nersc/": [
        {
          text: "At NERSC",
          items: [
            { text: "Quickstart",          link: "/nersc/index" },
            { text: "(not-yet-)Public Installation", link: "/nersc/public_installation" },
            { text: "User's Installation", link: "/nersc/users_installation" },
          ],
        },
        {
          text: "Step-by-step Guides",
          items: [
            { text: "JupyterHub", link: "/nersc/jupyter_at_nersc" },
            { text: "QuickView", link: "/nersc/perlmutter-run-quickview" },
            {
              text: "QuickCompare",
              link: "/nersc/perlmutter-run-quickcompare",
            },
          ],
        },
      ],
      "/guides/": [
        {
          text: "Introduction",
          items: [
            { text: "Key Reminders",      link: "/guides/reminders" },
            { text: "Connecitiviy Files", link: "/guides/connectivity" },
            { text: "Simulation Files",   link: "/guides/simulation_data" },
            { text: "Install and Launch", link: "/guides/install_and_launch" },
          ],
        },
        {
          text: "QuickView",
          items: [
            { text: "Resources",        link: "/guides/quickview/resources" },
            { text: "Keyboard Shortcuts",link: "/guides/quickview/shortcuts" },
            { text: "Toolbar",          link: "/guides/quickview/toolbar" },
            { text: "Control Panels",   link: "/guides/quickview/control_panels" },
            { text: "Viewport",         link: "/guides/quickview/viewport" },
          ],
        },
        {
          text: "QuickCompare",
          items: [
            { text: "Resources", link: "/guides/quickcompare/resources" },
            { text: "Getting started", link: "/guides/quickcompare" },
          ],
        },
        {
          text: "For app Developers",
          items: [
            { text: "Setup", link: "/guides/dev/setup" },
            { text: "Continuous Integration", link: "/guides/dev/ci" },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/Kitware/QuickView" },
    ],
  },

  markdown: {
    // Options for the Table of Contents plugin
    toc: { 
      level: [2, 3] // Only include <h2> and <h3> in the TOC
    },
    // Options for heading anchors (optional)
    anchor: {
      permalink: true // Enables clickable anchor links on headings
    }
  },

});
