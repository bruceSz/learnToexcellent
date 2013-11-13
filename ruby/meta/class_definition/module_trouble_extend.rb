module MyModule
	def my_method; 'hello';end
end

obj = Object.new
obj.extend MyModule
obj.my_method

class MyClass
	extend MyModule
end

MyClass.my_method
