path="tmp.txt"
fs = require "fs"
contents = fs.readFileSync path,"utf8"
strs = contents.split(",")
names = strs.map (str)->str[1..str.lenth-2]
names = names.sort()
vals = names.map (name)->name.split('')
vals = vals.map (list)->
    list.map(ch)->
        1+ch.charCodeAt(0)-'A'.charCodeAt(0)

vals = vals.map(list)->
    list.reduce (a,b)->a+b

vals = ((i+1)*vals[i] for i in [0...vals.length])
total = vals.reduce (a,b)-> a+b

console.log total
