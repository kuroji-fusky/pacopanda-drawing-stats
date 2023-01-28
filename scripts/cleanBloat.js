import fs from "fs"

const dirs = [".", "./apps/website", "./apps/api", "./puppeteer"]

dirs.forEach((dir) => {
	const prependNode = `${dir}/node_modules`

	console.log(`Deleting ${prependNode}...`)
	fs.rmSync(prependNode, { recursive: true, force: true })
})
