module Printable
	def print
		puts "print in printable"
	end

	def prepare_cover
		puts "prepare_cover in printable"
	end
end

module Document
	def print_to_screen
		prepare_cover
		format_for_screen
		print
	end

	def format_for_screen
		puts "format for screen in Document"
	end

	def print
		puts "print in Document"
	end
end

class Book
	include Document
	include Printable
end
