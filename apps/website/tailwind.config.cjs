/** @type {import('tailwindcss').Config} */
const sharedConfig = require("@pds/ui/tailwind.config.cjs")

module.exports = {
	content: ["./components/**/*.{js,vue,ts}"],
	...sharedConfig,
}
