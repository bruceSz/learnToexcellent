#class Loan
#	def initialize(book)
#		@book = book
#		@time = Time.new
#	end
#
#	def to_s
#		"#{@book.upcase} loaned on #{@time}"
#	end
#end

class Loan
	def initialize(book)
		@book = book
		@time = Loan.time_class.now

	end

	def self.time_class
		@time_class || Time
	end

	def to_s
	end
end

class FakeTime
	def self.now; '111';end
end

require 'test/unit'

class TestLoan < Test::Unit::TestCase
	def test_conversion_to_string
		Loan.instance_eval {@time_class = FakeTime}
		loan = Loan.new('war and peace')
		assert_equal '111',loan.to_s
	end
end

