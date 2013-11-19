class SimpleDelegator
	preserved = ["__id__","object_id","__send__","respond_to?"]
	instance_methods.each do |m|
		next if preserved.include?(m)
		undef_method m
	end

	def initialize(obj)
		@_sd_obj = obj
	end

	def method_missing(m,*args)
		unless @_sd_obj.respond_to?(m)
			super(m,*args)
		end
		@_sd_obj.__send__(m,*args)
	end

	def respond_to?(m)
		return true if super
		return @_sd_obj.respond_to?(m)
	end
end


