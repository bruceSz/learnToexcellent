v1 = 1

class MyClass
    v2 = 2
    print local_variables
    puts

    def my_method
	v3 = 3
	print 'in my_method',local_variables
	puts
    end

    print local_variables
    puts
end

obj = MyClass.new
obj.my_method
obj.my_method
print local_variables

