const BASE_URL = "https://www.furaffinity.net/gallery/pacopanda/"

import puppeteer from "puppeteer"
;(async () => {
	const browser = await puppeteer.launch()
	const navigatePage = await browser.newPage()

	const galleryPage = await navigatePage.goto(BASE_URL)

    /**
     * TODO This page uses pagination.
     * TODO recursively find the "Next" button until the element doesn't anymore,
     * TODO append it to a variable and then go through the usual stuff
     */
    let totalPages = 0;

	// This line should be kept at the bottom at all times unless an exception has thrown.
	await browser.close()
})()
