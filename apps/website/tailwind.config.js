/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme")
const basePlugin = require("tailwindcss/plugin")

module.exports = {
	content: [
		"./components/**/*.{js,vue,ts}",
		"./layouts/**/*.vue",
		"./pages/**/*.vue",
		"./plugins/**/*.{js,ts}",
		"./nuxt.config.{js,ts}",
		"./app.vue",
	],
	theme: {
		fontFamily: {
			inter: ["Inter", ...defaultTheme.fontFamily.sans],
			"open-sans": ["Open Sans", ...defaultTheme.fontFamily.sans],
			"jetbrains-mono": ["JetBrains Mono", ...defaultTheme.fontFamily.mono],
		},
	},
	plugins: [
		basePlugin(({ addBase, addComponents, theme }) => {
			addBase({
				html: {
					scrollBehavior: "smooth",
					overflowX: "hidden",
					"@media (prefers-reduced-motion)": {
						scrollBehavior: "auto",
					},
				},
				body: {
					fontFamily: theme("fontFamily.open-sans"),
					fontWeight: 500,
				},
			}),
				addComponents({
					".link-underline": {
						"text-decoration": "underline",
						color: theme("colors.green.500"),
						"&:hover": {
							color: theme("colors.green.700"),
						},
					},
				})
		}),
		require("@tailwindcss/typography"),
	],
}
