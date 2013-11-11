class MyClass
	@my_var = 1
	def self.read; @my_var;end
	def write;@my_var=2;end
	def read;@my_var;end
end

obj = MyClass.new
obj.write
puts obj.read
puts MyClass.read
obj1 = MyClass.new
obj1.write
puts obj1.read
