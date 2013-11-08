class MyClass
	define_method :my_method do |my_arg|
		my_arg*3
	end

	puts "define the MyClass"
end
obj = MyClass.new
puts obj.my_method(2)
