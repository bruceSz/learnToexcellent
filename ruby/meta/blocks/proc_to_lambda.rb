def double(callable_object)
	callable_object.call*2
end

l = lambda {return 10}
puts double(l)

def another_double
	p = Proc.new {return 10}
	result = p.call
	return result * 2
end

puts another_double

def another_another_double(callable_object)
	callable_object.call*2
end
p = Proc.new {10}
puts another_another_double(p)
