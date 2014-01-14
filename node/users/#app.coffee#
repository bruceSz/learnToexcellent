express = require "express"
redis = require "redis"
db = redis.createClient()
app = express()

app.use (req,res,next) ->
	ua = req.headers['user-agent']
	db.zadd 'online', Date.now(),ua,next

app.use (req,res,next) ->
	min = 60*1000
	ago = Date.now() - min
	db.zrevrangebyscore 'online', '+inf', ago, (err,users)->
			    	      return next(err) if err?
				      req.online = users
				      next

app.get '/',(req,res)->
	res.send req.online.length+' users online'

app.listen(3000)
			    