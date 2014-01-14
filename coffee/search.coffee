search = (keyword,cb)->
    host = "http://www.google.com.hk/"
    url = "#q=#{keyword}&safe=strict"
    $.getJSON url ,(json)->
        cb json.results

cb= (results)->
    console.log results

search "this",cb
