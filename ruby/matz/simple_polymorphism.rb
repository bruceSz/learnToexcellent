# bad example: hard to maintain this piece of code.
def box_open(box)
	if box_type(box) == "plain"
		puts "open it"
	elsif
		puts "open it with lock"
	elsif
		puts "unbuckele belt,open it"
	else
		puts "don't know how to open it,suck it!"
	end
end

def box_open2(box)
	box.open
end
box1 = Object.new
box2 = Object.new
box3 = Object.new
def box1.open
	puts "open it"
end

def box2.open
	puts "open it with lock"
end

def box3.open
	puts "unbuckele belt,open it"
end

box_open2(box1)

