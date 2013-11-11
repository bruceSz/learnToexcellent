class MyClass
	def method_one
		def method_two;'hello!';end
	end
end

obj = MyClass.new
puts obj.method_one
puts obj.method_two
