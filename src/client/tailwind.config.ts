import type { Config } from "tailwindcss"
import typographyPlugin from "@tailwindcss/typography"

const extendDefaults = {
  fonts: ["system-ui", "sans-serif"],
  unset: {
    unset: "unset",
  },
}

export default {
  darkMode: "class",
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
    "./nuxt.config.ts",
  ],
  theme: {
    extend: {
      fontFamily: {
        heading: ["Inter", ...extendDefaults.fonts],
        body: ["Open Sans", ...extendDefaults.fonts],
      },
      inset: extendDefaults.unset,
      spacing: extendDefaults.unset,
      margin: extendDefaults.unset,
    },
  },
  plugins: [typographyPlugin],
} as Config
