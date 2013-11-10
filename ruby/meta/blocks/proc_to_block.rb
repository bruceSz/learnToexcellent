def my_method(greeting)
    puts "#{greeting},#{yield}"
end

my_proc = proc {:bill}

my_method("hello",&my_proc)
