const withTM = require("next-transpile-modules")(["biro-ui-react"]);

module.exports = withTM({
  swcMinify: true,
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.target = 'electron-renderer';
    }

    return config;
  },
});
