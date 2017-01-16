bread = int(raw_input("How many slices of bread do you have? "))
pb = int(raw_input("How many sandwiches worth of peanut butter do you have? "))
jelly = int(raw_input("How many sandwiches worth of jelly do you have? "))
bread_sandwiches = bread/2
pbj_sand = min(bread_sandwiches, pb, jelly)
pb_sand = min(bread_sandwiches, pb)
sand_count = 0

while pbj_sand > 0:
	sand_count = sand_count + 1
	pbj_sand = pbj_sand - 1
	bread = bread - 2
	pb = pb - 1
	jelly = jelly - 1
	print "Making sandwich #{0}".format(sand_count)
	print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more sandwiches, and enough jelly for {2} more sandwiches".format(bread/2, pb, jelly)

if pb == 0 and jelly == 0 and bread/2 < 2:
	print "All done! Only had enough ingredients for {0} sandwiches.".format(sand_count)
elif pb == 0 and jelly == 0:
	print "All done! Only had enough peanut butter and jelly for {0} sandwiches.".format(sand_count)
elif pb == 0 and bread/2 < 2:
	print "All done! Only had enough peanut butter and bread for {0} sandwiches.".format(sand_count)
elif jelly == 0 and bread/2 < 2:
	print "All done! Only had enough jelly and bread for {0} sandwiches.".format(sand_count)
elif pb == 0:
	print "All done! Only had enough peanut butter for {0} sandwiches.".format(sand_count)
elif jelly == 0:
	print "All done! Only had enough jelly for {0} sandwiches.".format(sand_count)
elif bread/2 > 2:
	print "All done! Only had enough bread for {0} sandwiches.".format(sand_count)