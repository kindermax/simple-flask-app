var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var staticRoot = './static';

module.exports = {
    context: path.resolve(__dirname, staticRoot),
    entry:'./js/app.js',
    output: {
        path: path.resolve(__dirname, staticRoot, './assets'),
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js', '.css'],
        modules: [
            'node_modules',
        ]
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: '/node_modules/'
            },
            {
                test: /\.css$/i,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: 'css-loader',
                })
            },
            {
                test: /\.(jpe?g|ico|gif|png)$/,
                use: [
                    'file-loader'
                ]
            },
            {
                test: /\.(eot|woff(2)?|ttf|svg)$/,
                use: [
                    'file-loader'
                ]
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: "bundle.css",
        }),
        new webpack.ProvidePlugin({
            '$': 'jquery',
            jQuery: "jquery",
            "window.jQuery": "jquery",
        })
    ]
};