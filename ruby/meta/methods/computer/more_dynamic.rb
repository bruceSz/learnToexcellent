class Computer
	def initialize(computer_id,data_source)
		@id = computer_id
		@data_source = data_source
		data_source.methods.grep(/^grep_(.*)_info$/) {Computer.define_component $1}
	end

	def self.define_component(name)
		define_method(name) {
			info = @data_source.send "get_#{name}_info",@id
			price = @data_source.send "get_#{name}_price",@id
			result = "#{name.capitalize}: #{info} ($#{price})"
			return "* #{result}" if price >= 100
			result
		}
	end
end
