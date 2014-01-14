yearsOld = max:10,ida:9,tim:11

ages = for child,age of yearsOld
		console.log "#{child} is #{age}"
console.log ages

stdin = process.openStdin()
stdin.setEncoding 'utf8'

stdin.on 'data',(input)->
        name = input.trim()
        process.exit() if name == 'exit'
        console.log "Hello #{name}"
        console.log "Enter another name of 'exit' to exit"

console.log 'Enter your name'
