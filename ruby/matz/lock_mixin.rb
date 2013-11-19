module LockingMixin
	def lock
	end

	def unlock
	end
end

class Printer < Device
	include LockingMixin
	def spool(text)
		lock
			
		unlock
	end
end

