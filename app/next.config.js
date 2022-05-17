// @ts-check

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  compress: true,
  images: {
    domains: ['https://d.furaffinity.net'],
  }
}

module.exports = nextConfig

const PWASupport = require('next-pwa');

module.exports = PWASupport({
  pwa: {
    dest: 'public',
    register: true,
    skipWaiting: true,
    disable: process.env.NODE_ENV === 'development',
  }
});
