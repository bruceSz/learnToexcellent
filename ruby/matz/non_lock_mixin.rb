class Lock
	def lock
	end

	def unlock
	end
end

class Printer<Device
	def initialize
		@lock = Lock.new
	end

	def lock
		@lock.lock
	end

	def unlock
		@lock.unlock
	end

	def spool(text)
		lock
		unlock
	end
end
