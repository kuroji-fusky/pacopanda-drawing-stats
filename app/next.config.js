// @ts-check

/**
 *  @type {import('next').NextConfig} 
 **/
const nextConfig = {
  reactStrictMode: true,
  compress: true,
  images: {
    domains: ["https://d.furaffinity.net"]
  },
  i18n: {
    locales: ["en-us", "es"],
    defaultLocale: "en-us",
    localeDetection: false
  },
  compiler: {
    removeConsole: true
  }
}

module.exports = nextConfig
