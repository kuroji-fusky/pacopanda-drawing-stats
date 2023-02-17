/** @type {import('tailwindcss').Config} */
const sharedConfig = require("config/tailwind.config.cjs")

module.exports = {
	content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	...sharedConfig,
}