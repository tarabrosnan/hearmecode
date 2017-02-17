# Using for loop to loop from 99 to 1
# -1 tells the loop to decrease from 99 to 1 by 1 each loop
for number in range(99, 1, -1):

	# Prints the results for each loop
	print """{0} bottles of beer on the wall, {0} bottles of beer ...
			If one of those bottles should happen to fall, {1} bottles of beer on the wall""".format(number, number-1)
