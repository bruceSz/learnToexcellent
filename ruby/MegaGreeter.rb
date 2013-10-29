class MegaGreeter
	attr_accessor :names

	def initialize(names = "world")
		@@names = names
	end

	def say_hi
		if @names.nil?
			puts "..."
		elsif @names.respond_to?("each")
			@names.each do |name|
				puts "hello #{name}"
			end
		else
			puts "hello #{@names}"
		end
	end
	def say_bye
		if @names.nil?
			puts "..."
		elsif @names.respond_to?("join")
			puts "goodbye #{@names.join(",")}. come	back"
		else
			puts "goodbye #{@names}. come back soon"
		end
	end
end

if __FILE__ == $0
	mg = MegaGreeter.new
	mg.say_hi
	mg.say_bye

	mg.names = "zeke"
	mg.say_hi
	mg.say_bye

	mg.names = [ "albert" ,"brenda","charles","dave","engelbert"]
	mg.say_hi
	mg.say_bye

	mg.names = nil
	mg.say_hi
	mg.say_bye
end
