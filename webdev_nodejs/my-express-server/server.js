//jshint esversion:6

const express = require("express");

const app = express();

app.get("/", function(req, res){
    console.log(req);
    res.send("<h1>hello world</h1>");
});

app.get("/contact", function(req, res){
    res.send("cotact me at jordiibayo@gmail.com");
});

app.get("/about", function(req, res){
    res.send("my name is jordy bayo and i love beer and code");
});

app.listen(3000, function(){
    console.log("server stated on port 3000");
});

