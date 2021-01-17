const DotenvPlugin = require('dotenv-webpack')

module.exports = {
  webpack: (config) => {
    config.plugins.push(new DotenvPlugin());
    return config;
  }
};
