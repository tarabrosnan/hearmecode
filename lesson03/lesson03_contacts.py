# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
	'Shannon': {'phone': '202-555-5555', 'twitter': '@svt827', 'github': '@shannonturner'},
	'Tara': {'phone': '702-555-5555', 'twitter': '@tarabrosnan', 'github': '@tarabrosnan'},
	'Beyonce': {'phone': '303-555-5555', 'twitter': '@beyonce', 'github': '@bey'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

#for key, value in contacts.items():
#	print "{0}'s contact info: ".format(key)
#	for nested_key, nested_value in value.items():
#		print "\t{0}: {1}".format(nested_key, nested_value)

# Goal 2:  Display that information as an HTML table.
# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.


with open("contact_info.html", "w") as contact_info_file:
	for key, value in contacts.items():
		contact_info_file.write("""<table border="1">""")
		contact_info_file.write("""<tr>""")
		contact_info_file.write(("""<td colspan="2"> {0} </td>""".format(key)))
		contact_info_file.write("""</tr>""")
		contact_info_file.write("""<tr>""")
		for nested_key, nested_value in value.items():
			contact_info_file.write(("""<td> {0}: {1} </td>""".format(nested_key, nested_value)))
		contact_info_file.write("""</tr>""")
		contact_info_file.write("""</table>""")

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).