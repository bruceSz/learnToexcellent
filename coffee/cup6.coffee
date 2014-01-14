http = require "http"
fetchPage = (host,port,path,callback)->
    options =
        host:host
        port:port
        path:path
    req = http.get options,(res)->
        contents = ""
        res.on 'data',(chunk)->
            contents += "#{chunk}"
        res.on 'end',()->
            callback(contents)
    req.on "error",(e)->
        console.log "Error:{e.message}"

