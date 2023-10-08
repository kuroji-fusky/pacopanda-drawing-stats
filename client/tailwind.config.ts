import type { Config } from "tailwindcss";
import typographyPlugin from "@tailwindcss/typography";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      fontFamily: {
        heading: ["Inter", "system-ui", "sans-serif"],
        body: ["Open Sans", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [typographyPlugin],
} as Config;
