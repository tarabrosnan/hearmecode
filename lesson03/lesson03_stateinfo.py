# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# Sample output:

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

with open("state_info.csv", "r") as state_info:
	state_info = state_info.read().split("\n")

for index, row in enumerate(state_info):
	state_info[index] = row.split(",")

for state in state_info:
	with open("lesson03_stateinfo.html", "a") as stateinfo_html:
		stateinfo_html.write(""""<table border="1">
				<tr>
				<td colspan="2"> {0} </td>
				</tr>
				<tr>
				<td> Population Rank: {1} </td>
				<td> Percent: {2} </td>
				</tr>
				<tr>
				<td> US House Members: {3} </td>
				<td> Population: {4} </td>
				</tr>
				</table>""".format(state[1],state[0],state[4],state[3],state[2]))
