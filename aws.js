var fs = require('fs');

var AWS = require('aws-sdk');

AWS.config.update({
    accessKeyId: "AKIAINNWZYD2Z7GBSZLA",
    secretAccessKey: "MpHGFodyoTJFkBjIvs5BFC6QiX2Z/9a7RzfETj9Y",
    //"region": "sa-east-1"   <- If you want send something to your bucket, you need take off this settings, because the S3 are global. 
});


var s3 = new AWS.S3({region: 'us-west-2'});

s3.getObject({
    Bucket: 'imdb-datasets',
    Key: 'documents/v1/current/title.crew.tsv.gz',
    RequestPayer: 'requester', 
},function(err, data) {
	"use strict";
    // Handle any error and exit

    if (err) {
    	console.log(err)
        return err;
    }

  // No error happened
  // Convert Body from a Buffer to a String

  //let objectData = data.Body.toString('utf-8'); // Use the encoding necessary

  //console.log(objectData);
  console.log("begin write");
  fs.writeFile("title.crew.tsv.gz",data.Body,function(error) {
  	if (error) {
  		console.log(error);
  	}
  })
  console.log("end write");
});