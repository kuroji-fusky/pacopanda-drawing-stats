// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  modules: [
    [
      "@nuxt/image",
      {
        quality: 85
      }
    ],
    "@nuxt/content",
    [
      "nuxt-simple-sitemap",
      {
        exclude: ["api/**"],
        credits: false
      }
    ],
    "nuxt-lucide-icons",
    "nuxt-headlessui",
    "nuxt-lodash"
  ],
  app: {
    head: {
      htmlAttrs: {
        lang: "en"
      },
      script: [],
      link: [
        {
          rel: "shortcut icon",
          sizes: "128x128",
          type: "image/x-icon",
          href: "/favicon.ico"
        }
      ],
      bodyAttrs: {
        class: ""
      }
    }
  },
  build: {
    transpile: ["gsap"]
  },
  css: ["~/assets/global.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
      ...(process.env.NODE_ENV === "production" ? { cssnano: {} } : {})
    }
  }
})
