#!/usr/bin/node

var fs = require('fs');
var filename = process.argv[2]

fs.readFile(filename, 'utf8', function (err, data) {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data);
})
