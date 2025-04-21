movies = {
  "Ocean's Eleven" => 3.5,
  }

puts "What do you want to do?"

choice = gets.chomp

case choice
  when "add"
    puts "What movie do you want to add?"
    title = gets.chomp.to_sym
    puts "Rate this movie from 1 to 4:"
    rating = gets.chomp.to_i
    movies[title] = rating
    puts "Movie was added!"
  when "update"
    puts "Updated!"
  when "display"
    puts "Movies!"
  when "delete"
    puts "Deleted!"
  else puts "Error!"
end