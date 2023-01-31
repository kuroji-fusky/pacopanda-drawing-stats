import puppeteer from "puppeteer"
import fs from "fs"

const args = [
	"--disable-background-networking",
	"--disable-background-timer-throttling",
	"--no-first-run",
	"--no-sandbox"
]

const BASE_URL = "https://www.furaffinity.net/gallery/pacopanda/"
let TOTAL_PAGES = 1

;(async () => {
	const browser = await puppeteer.launch({
		args: args
	})

	const page = await browser.newPage()

	await page.goto(BASE_URL)

	const isNext = await page.evaluate(() => {
		TOTAL_PAGES = 1

		// prettier-ignore
		const query = `.submission-list form[action="/gallery/pacopanda/${TOTAL_PAGES+1}/"]`
		return document.querySelector(query)
	})

	while (isNext) {
		let url = `${BASE_URL}${TOTAL_PAGES}/?`
		await page.goto(url)

		TOTAL_PAGES++

		let query = `.submission-list form[action="/gallery/pacopanda/${TOTAL_PAGES}/"]`
		await page.$eval(query, (e) => console.log(e))

		console.log("Found page", TOTAL_PAGES)
	}

	await browser.close()
})()
