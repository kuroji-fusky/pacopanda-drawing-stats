const sharedConfig = require("@pds/config/tailwind.config.cjs")
/** @type {import('tailwindcss').Config} */
<<<<<<< HEAD
const sharedConfig = require("pds-custom-config/tailwind.config.cjs")
=======
>>>>>>> ac36948b229c1d8efe2b014c22dd8f1f4fab20e9

module.exports = {
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	...sharedConfig,
}
