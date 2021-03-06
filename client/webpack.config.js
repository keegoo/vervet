var webpack = require('webpack');
var path = require('path')
 
module.exports = {
  entry: './src/App.jsx',
  output: {
    filename: 'bundle.js',
    path: __dirname + '/build'
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        query: {
          plugins: ['transform-class-properties'],
          presets: ['es2015', 'react'],
        }
      }
    ]
  },
  resolve: {
    alias: {
      srcDir: path.resolve(__dirname, 'src/')
    }
  }
};