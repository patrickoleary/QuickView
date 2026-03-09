import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/QuickView",
  title: "E3SM QuickView",
  description:
    "How to start with the E3SM QuickView suite to look at your climate data",
  head: [["link", { rel: "stylesheet", href: "/custom.css" }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    search: {
      provider: "local",
    },
    logo: "/icon-full.png",
    nav: [
      { text: "Home", link: "/" },
      { text: "NERSC", link: "/nersc/login" },
      { text: "Guides", link: "/guides/data" },
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
            { text: "Data Format", link: "/guides/data" },
            { text: "Installation", link: "/guides/installation" },
          ],
        },
        {
          text: "Quick View",
          items: [
            { text: "Getting started", link: "/guides/quickview" },
            { text: "Resources", link: "/guides/quickview/resources" },
          ],
        },
        {
          text: "Quick Compare",
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
