
var express = require('express');
var app = express();

app.get('/',function(req,res){
    var body = 'hello world'
    res.setHeader('Content-Type','text/plain');
    res.setHeader('Content-Type',body.length);
    res.end(body)
});

app.get('/person',function(req,res){
    res.send({name:"zhang song",age:40});
});

app.listen(3000);

