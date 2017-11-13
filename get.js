// var http = require("http");
// var https = require("https");

var options = {
    host: 'imdb-datasets.s3.amazonaws.com',
    port: 443,
    path: '/documents/v1/*',
    method: 'GET',
    headers: {
        'Date' : "10222017",
        'Authorization' : 'AKIAJFPVEPYKKDYMYC2A',
        'x-amz-request-payer': 'requestor'
    }
};


/**
 * getJSON:  REST get request returning JSON object(s)
 * @param options: http options object
 * @param callback: callback to pass the results JSON object(s) back
 */
var http = require('http');


var req = http.get(options, function(res) {
  console.log('STATUS: ' + res.statusCode);
  console.log('HEADERS: ' + JSON.stringify(res.headers));

  // Buffer the body entirely for processing as a whole.
  var bodyChunks = [];
  res.on('data', function(chunk) {
    // You can process streamed parts here...
    bodyChunks.push(chunk);
  }).on('end', function() {
    var body = Buffer.concat(bodyChunks);
    console.log('BODY: ' + body);
    // ...and/or process the entire body here.
  })
});

req.on('error', function(e) {
  console.log('ERROR: ' + e.message);
});