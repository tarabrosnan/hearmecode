# Create list of state names
# source: http://weburge.com/build/states.php
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","District Of Columbia","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# Create list of state abbreviations
# source: http://weburge.com/build/states.php
state_abbr = ['AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

# Print results to generate html code
print "<select>"

# zip together list of states and state abbreviations so the correct combination prints for each loop
for state_abbr,state in zip(state_abbr,states):
	print """<option value="{0}">{1}</option>""".format(state_abbr,state)
print "</select>"