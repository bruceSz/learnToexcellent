def my_method
    x = "goodbye"
    yield("cruel")
end

x = "hello"
puts my_method {|y| "#{x}, #{y} world"}

def my_method2
    yield(2)
end

x = 1
 my_method2 do |x|
    x +=1
    puts x
    
 end
 puts x
