address1 = raw_input("Enter an address: ")
address2 = raw_input("Enter a second address: ")
address3 = raw_input("Enter a third and final address: ")

address1_list = address1.split(" ")
address2_list = address2.split(" ")
address3_list = address3.split(" ")

NW_list = []
NE_list = []
SE_list = []
SW_list = []

if "NW" in address1_list:
	NW_list.append(address1)
elif "NE" in address1_list:
	NE_list.append(address1)
elif "SE" in address1_list:
	SE_list.append(address1)
elif "SW" in address1_list:
	SW_list.append(address1)

if "NW" in address2_list:
	NW_list.append(address2)
if "NE" in address2_list:
	NE_list.append(address2)
if "SE" in address2_list:
	SE_list.append(address2)
if "SW" in address2_list:
	SW_list.append(address2)

if "NW" in address3_list:
	NW_list.append(address3)
if "NE" in address3_list:
	NE_list.append(address3)
if "SE" in address3_list:
	SE_list.append(address3)
if "SW" in address3_list:
	SW_list.append(address3)

if len(NW_list) == 1:
	print "1 NW address was entered. Here is the NW address: {0}".format(NW_list)
elif len(NW_list) > 1:
	print "{0} NW addresses were entered. Here are the NW addresses: {1}".format(len(NW_list), NW_list)
else:
	print "No NW addresses were entered."

if len(NE_list) == 1:
	print "1 NE address was entered. Here is the NE address: {0}".format(NE_list)
elif len(NE_list) > 1:
	print "{0} NE addresses were entered. Here are the NE addresses: {1}".format(len(NE_list), NE_list)
else:
	print "No NE addresses were entered."

if len(SE_list) == 1:
	print "1 SE address was entered. Here is the SE address: {0}".format(SE_list)
elif len(SE_list) > 1:
	print "{0} SE addresses were entered. Here are the SE addresses: {1}".format(len(SE_list), SE_list)
else:
	print "No SE addresses were entered."

if len(SW_list) == 1:
	print "1 SW address was entered. Here is the SW address: {0}".format(SW_list)
elif len(SW_list) > 1:
	print "{0} SW addresses were entered. Here are the SW addresses: {1}".format(len(SW_list), SW_list)
else:
	print "No SW addresses were entered."