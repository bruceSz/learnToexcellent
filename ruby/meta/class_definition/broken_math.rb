class Fixnum
	alias :old_plus :+

	def +(num)
		old_plus(num.old_plus(1))
	end

end

puts 1+1
