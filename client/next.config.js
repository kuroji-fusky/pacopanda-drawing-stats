const withMDX = require("@next/mdx")({
  options: {
    extension: /\.mdx?$/,
    providerImportSource: "@mdx-js/react",
  },
})

const withPWA = require("next-pwa")({
  dest: "public",
  register: true,
  skipWaiting: true,
})

/** @type {import('next').NextConfig} */
const nextConfig = {
  swcMinify: true,
  poweredByHeader: false,
  transpilePackages: ["lodash-es"],
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: "inline",
  },
}

module.exports = withMDX({
  pageExtensions: ["js", "jsx", "ts", "tsx", "md", "mdx"],
  ...withPWA(nextConfig),
})
