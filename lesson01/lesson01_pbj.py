bread = int(raw_input("How many slices of bread do you have? "))
pb = int(raw_input("How many sandwiches worth of peanut butter do you have? "))
jelly = int(raw_input("How many sandwiches worth of jelly do you have? "))
bread_sandwiches = bread/2
pbj_sand = min(bread_sandwiches, pb, jelly)
pb_sand = min(bread_sandwiches, pb)

if bread == 0 and pb == 0 and jelly == 0:
	print "You're out of bread, peanut butter, and jelly. No lunch for you today!"
elif bread == 0 and pb == 0:
	print "You're out of bread and peanut butter. No lunch for you today!"
elif bread == 0 and jelly == 0:
	print "You're out of bread and jelly. No lunch for you today!"
elif pb == 0 and jelly == 0:
	print "You're out of peanut butter and jelly, but you have {0} slices of bread. Looks like you can have toast for lunch!".format(bread)
elif pb == 0:
	print "You're out of peanut butter. No lunch for you today!"
elif bread == 0:
	print "You're out of bread. No lunch for you today!"
elif bread == 1 and pb == 1 and jelly == 1:
	print "You can't make a full PB&J, but you can make an open-faced PB&J!"
elif jelly == 0 and pb >=1 and bread_sandwiches >= 1:
	print "You're out of jelly, but you can make this many peanut butter sandwiches: {0}".format(pb_sand)
elif pbj_sand >= 1:
	print "You can make this many PB&Js for lunch: {0}".format(pbj_sand)
