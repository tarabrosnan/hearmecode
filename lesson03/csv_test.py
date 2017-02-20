import csv
delimiter = ','
contacts = {}

with open("contacts.csv", 'r') as contacts_file:
	reader = csv.reader(contacts_file)
	for row in reader:
		contacts[row[0]] = {row[i] for i in range(1, len(row))}

print contacts

#with open("contact_info.html", "w") as contact_info_file:
#	for key, value in contacts.items():
#		contact_info_file.write("""<table border="1">""")
#		contact_info_file.write("""<tr>""")
#		contact_info_file.write(("""<td colspan="2"> {0} </td>""".format(key)))
#		contact_info_file.write("""</tr>""")
#		contact_info_file.write("""<tr>""")
#		for nested_key, nested_value in value.items():
#			contact_info_file.write(("""<td> {0}: {1} </td>""".format(nested_key, nested_value)))
#		contact_info_file.write("""</tr>""")
#		contact_info_file.write("""</table>""")

