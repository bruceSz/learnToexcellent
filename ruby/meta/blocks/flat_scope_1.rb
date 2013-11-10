my_var = "Success"

class MyClass
    #puts "#{my_var}"
    puts @my_var

    def my_method
	puts $my_var
    end
end
