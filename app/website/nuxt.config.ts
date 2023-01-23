// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	modules: [
		"@nuxtjs/color-mode",
		"@nuxt/content",
		[
			"@pinia/nuxt",
			{
				autoImports: ["defineStore", ["defineStore", "definePiniaStore"]]
			}
		]
	],
	css: [
		"@fontsource/inter/400.css",
		"@fontsource/inter/600.css",
		"@fontsource/inter/700.css",
		"@fontsource/inter/800.css",
		"@fontsource/inter/900.css",
		"@fontsource/open-sans/400.css",
		"@fontsource/open-sans/400-italic.css",
		"@fontsource/open-sans/600.css",
		"@fontsource/open-sans/600-italic.css",
		"@fontsource/open-sans/800.css",
		"@fontsource/open-sans/800-italic.css",
		"~/assets/css/main.scss"
	],
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {}
		}
	},
	webpack: {
		optimizeCSS: true
	},
	typescript: {
		strict: true,
		shim: false
	}
})
