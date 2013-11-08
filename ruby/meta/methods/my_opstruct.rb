class MyOpenStruct
	def initialize
		@attributes = {}
	end

	def method_missing(name,*arg)
		attribute = name.to_s
		if attribute =~ /=$/
			@attributes[attribute.chop] = arg[0]
		else
			@attributes[attribute]
		end
	end
end
icecream = MyOpenStruct.new
icecream.flavor = "vanilla"
puts icecream.flavor

