# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>



#open file, read file in, split on new line
with open("state_info.csv", "r") as state_info_file:
	states_info = state_info_file.read().split("\n")

#for each state entry, split on comma to create a list of lists, one for each state entry
for index, entry in enumerate(states_info):
	states_info[index] = entry.split(",")

#data cleanup: remove extra quotes around state names (state[1]) and population percentages (state[4])
# This is done by removing first character ([1]) and last character ([-1])

for state in states_info:
	state[1] = state[1][1:-1]
	state[4] = state[4][1:-1]

with open("lesson03_stateinfo_2.html", "w") as html_file:
	for state in states_info[1:]:
		html_file.write("""<table border="1">""")	
		html_file.write("""<tr>""")
		html_file.write("""<td colspan="2"><b> {0} </b></td>""".format(state[1]))
		html_file.write("""</tr>""")
		html_file.write("""<tr>""")
		html_file.write("""<td> Rank: {0} </td>.""".format(state[0]))
		html_file.write("""<td> Percent: {0} </td>""".format(state[4]))
		html_file.write("""</tr>""")
		html_file.write("""<tr>""")
		html_file.write("""<td> U.S. House Members: {0} </td>""".format(state[3]))
		html_file.write("""<td> Population: {0} </td>""".format(int(state[2])))
		html_file.write("""</tr>""")
		html_file.write("""</table""")
	#html_file.write("""</table>""")

