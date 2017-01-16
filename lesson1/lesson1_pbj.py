bread_slices = raw_input("How many slices of bread do you have? ")
pb = raw_input("How many sandwiches worth of peanut butter do you have? ")
jelly = raw_input("How many sandwiches worth of jelly do you have? ")

bread_slices = int(bread_slices)
pb = int(pb)
jelly = int(jelly)
bread_sandwiches = bread_slices/2
total_pbj = min(bread_sandwiches, pb, jelly)
total_openfaced = min(bread_slices%2, pb, jelly)-total_pbj
total_pb = min(bread_sandwiches, pb)-total_pbj

# Goal 5: Which ingredients are you missing?
if bread_slices == 0 and pb == 0 and jelly == 0:
	print "You're out of bread, peanut butter, and jelly! Looks like no PB&J today."
elif bread_slices == 0 and pb == 0:
	print "You're out of bread and peanut butter! Looks like no PB&J today."
elif bread_slices == 0 and jelly == 0:
	print "You're out of bread and jelly! Looks like no PB&J today."
elif pb == 0 and jelly == 0:
	print "You're out of peanut butter and jelly! Looks like no PB&J today."
elif bread_slices == 0:
	print "You're out of bread! Looks like no PB&J today."
elif pb == 0:
	print "You're out of peanut butter! Looks like no PB&J today."
elif jelly == 0 and total_pb >= 1:
	print "You're out of jelly! But it looks like you can make this many PB sandwiches: {0}".format(total_pb)
elif (bread_slices%2 == 1
	and total_openfaced > 0):
	print """You can make this many PB&J sandwiches: {0}
	And this many open-faced PB&Js: {1}""".format(total_pbj, total_openfaced)
else:
	print "You can make this many PB&Js: {0}".format(total_pbj)


