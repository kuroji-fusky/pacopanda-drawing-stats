// @ts-check

/**
 *  @type {import('next').NextConfig}
 **/
module.exports = async (phase) => {
  const plugins = require("next-compose-plugins")
  const withMDX = require("@next/mdx")({
    extension: /\mdx?$/,
    options: {
      providerImportSource: "@mdx-js/react"
    }
  })

  const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    compress: true,
    images: {
      domains: ["https://d.furaffinity.net"],
      formats: ["image/webp"]
    },
    i18n: {
      locales: ["en-us", "es"],
      defaultLocale: "en-us",
      localeDetection: false
    },
  }

  const defaultConfig = {}

  return plugins(
    [
      withMDX({ pageExtensions: ["ts", "tsx", "md", "mdx"] })
    ], nextConfig
  )(phase, { defaultConfig })
}