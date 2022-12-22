/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        "inter": ["var(--font-inter", "Inter", ...defaultTheme.fontFamily.sans],
        "open-sans": ["var(--font-open-sans", "Open Sans", ...defaultTheme.fontFamily.sans],
        "jetbrains-mono": ["var(--font-jetbrains)", "JetBrains Mono", ...defaultTheme.fontFamily.mono]
      }
    },
  },
  plugins: [],
};