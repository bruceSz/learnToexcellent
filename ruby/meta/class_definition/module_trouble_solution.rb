module MyModule
	def my_method;'hello';end

end

class MyClass
	class << self
		include MyModule
	end
end

MyClass.my_method
