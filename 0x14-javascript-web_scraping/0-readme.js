#!/usr/bin/node

var fs = require('fs');
const { default: _ } = require('underscore/modules/underscore.js');
var filename = process.argv[1]

fs.readFile(filename, 'utf8', function (err, data) {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data);
    
})
