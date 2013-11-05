puts "This is the guess number world!~"
while true
    target = rand(10)
    puts "Please guess the number in my mind right now,just input it using your keyboard(-1 will exit ):"
    i = gets
    i=i.to_i

    if i==-1
	exit
    end

    while i!=target
	if i>target
	    puts "too big ,try a smaller one:"
	end
	if i<target
	    puts "too small,try a bigger one:"
	end
	i=gets
	i=i.to_i

	if i==-1
	    exit
	end
	
    end
    puts "you made it!"

end
