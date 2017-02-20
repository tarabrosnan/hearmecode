# Rules
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.
# Create a program that will generate the first 10 numbers in the Fibonacci Sequence.
# When completed, your program should have the output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Because I couldn't figure out how to do this starting from a blank list, 
# my list starts with the first two items of the Fibonnaci sequence
seq = [0, 1]

# Since I'm starting with the first two items, I only need a for loop for the next 8 numbers
for number in range(8):

# Since the next number in the sequence is the sum of the previous two, we need to define the previous two numbers
# Define num1 and num2 by slicing
# We want this to be dynamic for each loop, so we can use [-1] and [-2] to select the last two number in the sequence
	#num1 = seq[-1]
	#num2 = seq[-2]

# Sum num2 and num2 and append the result to the sequence, and then the loop continues
	seq.append(seq[-1]+seq[-2])

print seq