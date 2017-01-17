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

with open("state_info.csv", "r") as state_info_csv:
	state_info = state_info_csv.read()

with open("state_info.csv", "r") as state_info_csv:
	state_info = state_info_csv.read().split(",")

for index,state in enumerate(state_info):
	state_info[index] = state.split("\n")

print state_info




