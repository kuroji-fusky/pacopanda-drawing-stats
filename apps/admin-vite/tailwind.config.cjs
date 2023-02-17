const sharedConfig = require("ui/tailwind.config.cjs")
/** @type {import('tailwindcss').Config} */

module.exports = {
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	...sharedConfig,
}
