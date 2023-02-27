/** @type {import('tailwindcss').Config} */
const sharedConfig = require("@pds/config/tailwind.config.cjs")

module.exports = {
	content: ["./components/**/*.{js,vue,ts}"],
	...sharedConfig,
}
