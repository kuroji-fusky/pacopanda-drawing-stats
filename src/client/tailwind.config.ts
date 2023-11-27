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
  content: ["./src/**/*.{html,js,svelte,ts}"],
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
