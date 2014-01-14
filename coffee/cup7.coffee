path = require "path"
fs = require "fs"
serveStatic = (uri,res)->
    fileNmae = path.join process.cwd(),uri
