require 'highline'
hl = HighLine.new
friends = hl.ask("Friends?",lambda {|s| s.split(',')})
puts "you're friends with:#{friends.inspect}"

