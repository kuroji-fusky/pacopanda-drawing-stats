// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  modules: [
    "@nuxt/content",
    "@nuxt/image",
    "nuxt-lucide-icons",
    "nuxt-simple-sitemap",
    "nuxt-lodash",
  ],
  app: {
    head: {
      htmlAttrs: {
        lang: "en",
      },
      script: [],
      link: [
        {
          rel: "shortcut icon",
          sizes: "128x128",
          type: "image/x-icon",
          href: "/favicon.ico",
        },
      ],
      bodyAttrs: {
        class: "",
      },
    },
  },
  image: {
    quality: 85,
  },
  build: {
    transpile: ["gsap"],
  },
  css: ["~/assets/global.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})
