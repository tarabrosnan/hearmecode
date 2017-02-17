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

	# Conditional: looks for quadrant in "address" and adds the address to the appropriate list
	# What does the .join() do? I forget...
	if "NW" in address:
		nw_addresses.append(address)
	elif "NE" in address:
		ne_addresses.append(address)
	elif "SE" in address:
		se_addresses.append(address)
	elif "SW" in address:
		sw_addresses.append(" ".join(address))
	else:
		no_quadrant.append(" ".join(address))

print nw_addresses
print ne_addresses
print se_addresses
print sw_addresses
