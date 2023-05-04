//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");

const app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res){
    console.log(req.body.crypto);

    request("https://apiv2.bitcoinaverage.com/convert/global?from=BTC&to=USD&amount=1", function(error, response, body){
        console.log(response);
    });
});

app.listen(3000, function(){
    console.log("server is running on 3000");
});