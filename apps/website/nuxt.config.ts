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
			meta: [
				{ name: "X-UA-Compatible", content: "IE=edge" },
				{ name: "robots", content: "noindex,nofollow" },
			],
			link: [
				{ rel: "shortcut icon", href: "/favicon.ico" },
				{ rel: "manifest", href: "/manifest.webmanifest" },
			],
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

	// @nuxt/content
	content: {
		documentDriven: true,
	},
})
