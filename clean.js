import fs from "fs"

const nodeDirs = [
	"./apps/api",
	"./apps/website",
	"./apps/admin",
	"./scripts/puppeteer",
	".",
]

nodeDirs.forEach((dir) => {
	const prependNode = `${dir}/node_modules`

	console.log(`Deleting ${prependNode}...`)
	fs.rmSync(prependNode, { recursive: true, force: true })
})
