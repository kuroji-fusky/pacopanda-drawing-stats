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

  const runtimeCaching = require('next-pwa/cache')
  runtimeCaching[0].handler = 'StaleWhileRevalidate'

  const withPWA = require('next-pwa')({
    dest: "public",
    // disable: process.env.NODE_ENV === "development",
    register: true,
    runtimeCaching
  });

  const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    compress: true,
    images: {
      domains: ["https://d.furaffinity.net"],
      formats: ["image/webp"]
    },
    compiler: {
      removeConsole: process.env.NODE_ENV !== 'development',
    },
    i18n: {
      locales: ["en-us", "es"],
      defaultLocale: "en-us",
      localeDetection: true
    },
  }

  const defaultConfig = {}

  return plugins(
    [
      withMDX({ pageExtensions: ["ts", "tsx", "md", "mdx"] }),
      withPWA
    ], nextConfig
  )(phase, { defaultConfig })
}