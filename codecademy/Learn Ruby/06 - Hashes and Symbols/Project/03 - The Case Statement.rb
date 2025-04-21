movies = {
  "Ocean's Eleven" => 3.5,
  }

puts "What do you want to do?"

choice = gets.chomp

case choice
  when "add"
    puts "Added!"
  when "update"
    puts "Updated!"
  when "display"
    puts "Movies!"
  when "delete"
    puts "Deleted!"
  else puts "Error!"
end

#puts "--add"
#puts "--update"
#puts "--display"
#puts "--delete"