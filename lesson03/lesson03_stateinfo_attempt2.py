with open('states.txt','r') as states_file:
    states = states_file.read().split('\n')

states_html= ''
states_html += '<select>' 

for index,state in enumerate(states):
    states[index] = states[index].split('\t')
    states_html += '<option value="{0}">{1}</option>'.format(states[index][0],states[index][1])

states_html += '</select>'

with open("states_1.html", "w") as states_1_file:
	states_1_file.write(states_html)