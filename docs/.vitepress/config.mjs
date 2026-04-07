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
          text: "Connecting to NERSC",
          items: [
            { text: "Login", link: "/nersc/login" },
            { text: "Installation", link: "/nersc/installation" },
          ],
        },
        {
          text: "Perlmutter",
          items: [
            { text: "Quick View", link: "/nersc/perlmutter-run-quickview" },
            {
              text: "Quick Compare",
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
            { text: "Getting started", link: "/guides/quickcompare" },
            { text: "Resources", link: "/guides/quickcompare/resources" },
          ],
        },
        {
          text: "Development",
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
});
