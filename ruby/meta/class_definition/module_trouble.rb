module MyModule
	def my_method; 'hello';end
end

class MyClass
	include MyModule
end

MyClass.my_method

