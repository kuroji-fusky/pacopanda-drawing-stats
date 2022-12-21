/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        "inter": ["Inter", ...defaultTheme.fontFamily.sans],
        "open-sans": ["Open Sans", ...defaultTheme.fontFamily.sans],
        "jetbrains-mono": ["JetBrains Mono", ...defaultTheme.fontFamily.mono]
      }
    },
  },
  plugins: [],
};