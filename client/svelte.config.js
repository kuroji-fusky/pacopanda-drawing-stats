import adapter from "@sveltejs/adapter-auto"
import { vitePreprocess } from "@sveltejs/kit/vite"
import { mdsvex } from "mdsvex"

/** @type {import('mdsvex').MdsvexOptions} */
const mdsvexOptions = {
  extensions: [".md"],
}

/** @type {import('@sveltejs/kit').Config} */
export default {
  extensions: [".svelte", ".md"],
  preprocess: [vitePreprocess(), mdsvex(mdsvexOptions)],
  kit: {
    adapter: adapter(),
    csp: {
      mode: "nonce",
      directives: {
        "upgrade-insecure-requests": true,
      },
    },
  },
}
