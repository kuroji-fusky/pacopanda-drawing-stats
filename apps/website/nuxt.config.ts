import { resolve, dirname } from "node:path"
import { fileURLToPath } from "url"
import VueI18nVitePlugin from "@intlify/unplugin-vue-i18n/vite"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	modules: [
		"@nuxtjs/color-mode",
		"@nuxt/content",
		[
			"@pinia/nuxt",
			{
				autoImports: ["defineStore", ["defineStore", "definePiniaStore"]],
			},
		],
	],
	plugins: [{ src: "~/plugins/vercel.ts", mode: "client" }],
	build: {
		transpile: ["gsap"],
	},
	css: ["~/assets/css/main.scss"],
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {},
		},
	},
	webpack: {
		optimizeCSS: true,
	},
	vite: {
		plugins: [
			VueI18nVitePlugin({
				include: [
					resolve(dirname(fileURLToPath(import.meta.url)), "./locales/*.json"),
				],
			}),
		],
	},
	typescript: {
		strict: true,
		shim: false,
	},
})
