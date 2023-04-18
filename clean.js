import fs from "fs"

const options = { recursive: true, force: true }

const nodeDirs = ["./apps/api", "./apps/website", "."]

nodeDirs.forEach((dir) => {
	const prependNode = `${dir}/node_modules`

	console.log(`Deleting ${prependNode}...`)
	fs.rmSync(prependNode, options)
})

const websiteDir = nodeDirs[1]
const websiteTemps = [`${websiteDir}/.turbo`, `${websiteDir}/.output`]

websiteTemps.forEach((dir) => {
	console.log(`Deleting ${dir}...`)
	fs.rmSync(dir, options)
})
