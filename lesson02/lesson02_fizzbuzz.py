# Rules:
# Create a program that loops through the numbers 0-100.
# When you land on a number evenly divisible by 3, have your program print "Fizz"
# When you land on a number evenly divisible by 5, have your program print "Buzz"
# When you land on a number evenly divisible by both 3 and 5, have your program print "Fizzbuzz"
# When you land on any other number, print that number

# Create for loop to start at 0 and go to 100
for number in range(0, 101):

# Remember! The order of the conditional loop is important. Start with most stringent criteria and work down.

# If the number is evenly divisible by 3 AND 5
	if number%3 == 0 and number%5 == 0:
		print "FizzBuzz"

# If the number is divisible by 3 ONLY		
	elif number%3 == 0:
		print "Fizz"

# If the number is divisible by 5 ONLY		
	elif number%5 == 0:
		print "Buzz"

# If none of the above is true		
	else:
		print number