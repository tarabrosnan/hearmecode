# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

for index,state in enumerate(states):
	states[index] = state.split("\t")

state_abbr = [item[0] for item in states]
state_name = [item[1] for item in states]

with open("lesson03_states.html", "w") as states_html:
	states_html.write("<select>")


for state_abbr,state_name in zip(state_abbr,state_name):
	with open("lesson03_states.html", "a") as states_html:
		states_html.write(""""<option value="{0}">{1}</option>""".format(state_abbr,state_name))

with open("lesson03_states.html", "a") as states_html:
	states_html.write("</select>")

#print state_abbr
#print state_name
#print zip(state_abbr, state_name)
#print """"<select>
#	<option value="{0}">{1}</option>
#	</select>""".format(state_abbr,state_name)

#for state_abbr,state_name in zip(state_abbr,state_name):	
#	with open("lesson03_states.html", "a") as states_html:	
#		states_html.write(""""<select>
#	<option value="{0}">{1}</option>
#	</select>""".format(state_abbr,state_name))



