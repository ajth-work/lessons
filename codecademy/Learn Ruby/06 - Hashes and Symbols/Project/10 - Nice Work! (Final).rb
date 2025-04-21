movies = {
  "Ocean's Eleven" => 3.5,
  }

puts "What do you want to do?"
puts "-----------------------"

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
        puts "Error: Submitted rating is out of range."
        puts "Rate this movie from 1 to 4:"
        rating = gets.chomp.to_i 
        end
      movies[title] = rating
      puts "Movie was added!"
    end
  when "update"
    puts "Which title do you want to update?"
    title = gets.chomp
    if movies[title] == nil
      puts "Error: Movie does not exist."
    else puts "Update the rating for this movie from 1 to 4:" 
      rating = gets.chomp.to_i
      while rating < 1 || rating > 4
        puts "Error: Submitted rating is out of range."
        puts "Update the rating for this movie from 1 to 4:"
        rating = gets.chomp.to_i 
        end
      movies[title] = rating
      puts "Movie was updated!"
  end
  when "display"
    movies.each do |title, rating|
      puts "#{title}: #{rating}"
    end
    puts "-----------------------"
    puts "Displaying a total of #{movies.count} movie(s)."
  when "delete"
    puts "Which movie would you like to delete?"
    title = gets.chomp
    if movies[title] == nil
      puts "Error: Movie does not exist."
    else movies.delete(title.to_sym)
    end
    puts "#{title} was deleted."
  else puts "Error!"
end