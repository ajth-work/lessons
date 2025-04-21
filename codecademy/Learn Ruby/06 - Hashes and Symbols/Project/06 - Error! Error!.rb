movies = {
  "Ocean's Eleven" => 3.5,
  }

puts "What do you want to do?"

choice = gets.chomp

case choice
  when "add"
    puts "What movie do you want to add?"
    title = gets.chomp.to_sym
    if movies[title.to_sym] != nil
      puts "Error: This movie already exists."
    else 
      puts "Rate this movie from 1 to 4:"
      rating = gets.chomp.to_i
      while rating < 1 || rating > 4
        puts "Error: Submitted Rating is out of range."
        puts "Rate this movie from 1 to 4:"
        rating = gets.chomp.to_i 
        end
      movies[title] = rating
      puts "Movie was added!"
    end
  when "update"
    puts "Updated!"
  when "display"
    puts "Movies!"
  when "delete"
    puts "Deleted!"
  else puts "Error!"
end