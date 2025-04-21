puts "Hello there! What is your primary language?"
greeting = gets.chomp

# Add your case statement below!
case greeting.downcase
  when "english" then puts "Hello!"
  when "french" then puts "Bonjour!"
  when "german" then puts "Guten Tag!"
  when "finnish" then puts "Haloo!"
  else puts "I don't know that language!"
end