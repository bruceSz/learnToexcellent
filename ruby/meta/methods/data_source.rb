class DS
    def initialize # connect to data source
    def get_mouse_info(workstation_id) #..
    def get_mouse_price(workstation_id) # ..
    def get_keyboard_info(workstation_id)
    def get_keyboard_price(workstation_id)
    def get_cpu_info(workstation_id) #...
    def get_cpu_price(workstation_id) #..
    def get_display_info(workstation_id)
    def get_display_price(workstation_id)
end

class Computer
    def initialize(computer_id,data_source)    
	@id = computer_id
	@data_source = data_source
    end
    def mouse
	info = @data_source.get_mouse_info(@id)
	price = @data_source.get_mouse_price(@id)
	result = "Mouse: #{info} ($#{price})"
	return "#{result}" if price >= 100
	result
    end
    def keyboard
	info = @data_source.get_keyboard_info(@id)
	price = @data_source.get_keyboard_price(@id)
	result = "Keyboard: #{info} ($#{price})"
	return "#{result}" if price >= 100
	result
    end
end
