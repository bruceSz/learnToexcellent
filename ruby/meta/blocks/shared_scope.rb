def define_methods
    shared = 0

    Kernel.send :define_method,:counter do
	shared
    end

    Kernel.send :define_method,:inc do |x|
	shared +=x
    end
end
define_methods

puts counter 
inc(4)
puts counter
