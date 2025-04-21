def double(number)
	puts number
	yield(5)
	yield(12)
end

double(2) {|number| puts number * 2}