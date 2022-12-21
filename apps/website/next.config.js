/** @type {import('next').NextConfig} */
const withTM = require("next-transpile-modules")(["biro-ui-react"]);

module.exports = withTM({
  reactStrictMode: true,
  swcMinify: true,
})
