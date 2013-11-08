class MyClass
    def my_method(my_arg)
	my_arg * 2
    end
end
obj = MyClass.new
puts obj.my_method(3)
puts obj.send(:my_method,3)
