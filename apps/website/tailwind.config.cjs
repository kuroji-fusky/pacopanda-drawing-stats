/** @type {import('tailwindcss').Config} */
const sharedConfig = require("config/tailwind.config.cjs")

module.exports = {
	content: [
		"./components/**/*.{js,vue,ts}",
		"./layouts/**/*.vue",
		"./pages/**/*.vue",
		"./plugins/**/*.{js,ts}",
		"./nuxt.config.{js,ts}",
		"./app.vue",
	],
	...sharedConfig,
}
