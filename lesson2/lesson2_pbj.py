bread_slices = 4
pb = 3
jelly = 10
bread_sandwiches = bread_slices/2
sandwiches = min(bread_sandwiches, pb, jelly)
num_sandwich = 0

while sandwiches >= 1:
	num_sandwich = num_sandwich + 1
	sandwiches = sandwiches - 1
	print "Making sandwich #{0}".format(num_sandwich)

print "All done. Only had enough for {0} sandwiches".format(num_sandwich)