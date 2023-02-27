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
	app: {
		head: {
			htmlAttrs: {
				lang: "en",
			},
			link: [{ rel: "shortcut icon", href: "/favicon.ico" }],
			script: [
				{
					// prettier-ignore
					children: `
          (function(c,l,a,r,i,t,y){
          c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
          })(window, document, "clarity", "script", "${process.env.CLARITY_ID ?? 'NOT_SET'}");
          `,
				},
			],
		},
	},
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
})
