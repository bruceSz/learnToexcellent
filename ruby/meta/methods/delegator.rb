require 'delegate'

class Assistant
	def initialize(name)
		@name
	end

	def read_email
		"(#{@name}) It's  mostly spam."
	end

	def check_schedule
		"(#{@name}) you have a metting today"
	end
end

class Manager < DelegateClass(Assistant)
	def initialize(assistant)
		super(assistant)
	end

	def attend_meeting
		"Please hold my calls."
	end
end
frank = Assistant.new("Frank")
anne = Manager.new(frank)
puts anne.attend_meeting
