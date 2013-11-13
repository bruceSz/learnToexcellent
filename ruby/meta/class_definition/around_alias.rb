class String
	alias :real_length :length

	def length
		real_length > 5 ? 'long':'short'
	end
end

puts "war and peace ".length
puts "war and peace ".real_length
