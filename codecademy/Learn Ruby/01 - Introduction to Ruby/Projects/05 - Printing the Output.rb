print "What's your first name?"
first_name = gets.chomp
first_name = first_name.capitalize!

print "What's your last name?"
last_name = gets.chomp
last_name = last_name.capitalize!

print "What's your city name?"
city = gets.chomp
city = city.capitalize!

print "What's your abbreviated state/province name?"
state = gets.chomp
state = state.upcase!

puts "My name is #{first_name} #{last_name} and I live in #{city}, #{state} in Japan."