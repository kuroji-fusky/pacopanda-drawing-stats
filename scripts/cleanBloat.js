import fs from "fs"

const nodeDirs = [
  "./apps/website",
  "./apps/api",
  "./scripts/puppeteer",
  "."
]

nodeDirs.forEach((dir) => {
	const prependNode = `${dir}/node_modules`

	console.log(`Deleting ${prependNode}...`)
	fs.rmSync(prependNode, { recursive: true, force: true })
})
