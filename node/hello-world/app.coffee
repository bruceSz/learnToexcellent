express = require 'express'
app = express()

app.get 'hello.txt' , (req,res)->
	body = 'Hello world'
	res
		.setHeader 'Content-Type' , 'text/plain'
		.setHeader 'Content-Length' , body.length
		.end body

app.get '/hello.txt' , (req,res)->
	res.send 'hello world'

app.listen 3000

console.log 'Listening on port 3000'