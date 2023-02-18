<<<<<<< HEAD
/** @type {import('tailwindcss').Config} */
const sharedConfig = require("pds-custom-config/tailwind.config.cjs")
=======
const sharedConfig = require("@pds/config/tailwind.config.cjs")
>>>>>>> ac36948b229c1d8efe2b014c22dd8f1f4fab20e9

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
