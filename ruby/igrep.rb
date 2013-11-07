pattern=ARGV[0]
filename=ARGV[1]
if ARGV.length >2
    puts "Usage: pattern filename!"
    exit
end
f = File.open(filename,'r') do |f|
    while str=f.gets
	if str.include?(pattern)
	    puts str
	end
    end
end
