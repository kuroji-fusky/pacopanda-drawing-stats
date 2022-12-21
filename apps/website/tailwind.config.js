/** @type {import('tailwindcss').Config} */
const biroConfig = require("config/tailwind.config");

module.exports = {
  content: [
    "../../packages/biro-ui-react/**/*.{js,ts,jsx,tsx}",
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  ...biroConfig
}