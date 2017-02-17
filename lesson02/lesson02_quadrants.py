# Create empty lists for each quadrant, and one for no quadrant
nw_addresses = []
ne_addresses = []
se_addresses = []
sw_addresses = []
no_quadrant = []

# Create loop to ask to enter an address 3 times
for entry in range(3):
	# Raw input allows user to enter a response, stores it in the variable "address"
	address = raw_input("Enter an address: ")
	
	# Redefines address as a list of strings (split on spaces)
	# Converts all strings to uppercase
	address = address.upper().split(" ")

	# Conditional: looks for quadrant in "address" and appends to quadrant to the appropriate list
	# .join() undoes the .split() we originally used on order to parse out the quadrant, 
	# and allows the address to be added as one string to the quadrant address lists
	if "NW" in address:
		nw_addresses.append(" ".join(address))
	elif "NE" in address:
		ne_addresses.append(" ".join(address))
	elif "SE" in address:
		se_addresses.append(" ".join(address))
	elif "SW" in address:
		sw_addresses.append(" ".join(address))
	else:
		no_quadrant.append(" ".join(address))


# Printing our results!
if len(nw_addresses) == 1:
	print "1 NW address was entered. Here is the NW address: {0}".format(nw_addresses)
elif len(nw_addresses) > 1:
	print "{0} NW addresses were entered. Here are the NW addresses: {1}".format(len(nw_addresses), nw_addresses)
else:
	print "No NW addresses were entered."

if len(ne_addresses) == 1:
	print "1 NE address was entered. Here is the NE address: {0}".format(ne_addresses)
elif len(ne_addresses) > 1:
	print "{0} NE addresses were entered. Here are the NE addresses: {1}".format(len(ne_addresses), ne_addresses)
else:
	print "No NE addresses were entered."

if len(se_addresses) == 1:
	print "1 SE address was entered. Here is the SE address: {0}".format(se_addresses)
elif len(se_addresses) > 1:
	print "{0} SE addresses were entered. Here are the SE addresses: {1}".format(len(se_addresses), se_addresses)
else:
	print "No SE addresses were entered."

if len(sw_addresses) == 1:
	print "1 SW address was entered. Here is the SW address: {0}".format(sw_addresses)
elif len(sw_addresses) > 1:
	print "{0} SW addresses were entered. Here are the SW addresses: {1}".format(len(sw_addresses), sw_addresses)
else:
	print "No SW addresses were entered."

if len(no_quadrant) == 1:
	print "1 no quadrant address was entered. Here is the no quadrant address: {0}".format(no_quadrant)
elif len(no_quadrant) > 1:
	print "{0} no quadrant addresses were entered. Here are the no quadrant addresses: {1}".format(len(no_quadrant), no_quadrant)
else:
	print "No no quadrant addresses were entered."
