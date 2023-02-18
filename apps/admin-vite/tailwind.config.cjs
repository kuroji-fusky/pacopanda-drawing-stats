const sharedConfig = require("@pds/config/tailwind.config.cjs")
/** @type {import('tailwindcss').Config} */

module.exports = {
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	...sharedConfig,
}
