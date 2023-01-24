/** @type {import('tailwindcss').Config} */
const basePlugin = require("tailwindcss/plugin")
const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
	content: [
		"./components/**/*.{js,vue,ts}",
		"./layouts/**/*.vue",
		"./pages/**/*.vue",
		"./plugins/**/*.{js,ts}",
		"./nuxt.config.{js,ts}",
		"./app.vue"
	],
	theme: {
		fontFamily: {
			"inter": ["Inter", ...defaultTheme.fontFamily.sans],
			"open-sans": ["Open Sans", ...defaultTheme.fontFamily.sans]
		},
		extend: {}
	},
	plugins: [
		basePlugin(({ addBase, addComponents, theme }) => {
			addBase({
				html: {
					"scrollBehavior": "smooth",
					"overflowX": "hidden",
					"@media (prefers-reduced-motion)": {
						scrollBehavior: "auto"
					}
				},
				body: {
					fontFamily: theme("fontFamily.open-sans")
				}
			}),
			addComponents({
				".link-underline": {
					"text-decoration": "underline",
					"color": theme("colors.green.500"),
					"&:hover": {
						color: theme("colors.green.700")
					}
				}
			})
		}),
		require("@tailwindcss/typography")
	]
}
