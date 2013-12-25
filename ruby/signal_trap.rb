trap(:INT) {puts "This is  the first signal handler."}

old_handler = trap(:INT){
    puts "about to exit"
    old_handler.call
    exit
}
sleep
