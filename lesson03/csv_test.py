import csv

employee_dict = []
survey_dict = []
survey_emails = []

with open("all_employees.csv") as employees_file:
	fieldnames = ['name', 'email', 'phone', 'department', 'position']
	reader = csv.DictReader(employees_file)
	for row in reader:
		employee_dict.append(row)


with open("survey.csv") as survey_file:
	fieldnames = ['email', 'twitter', 'github']
	reader = csv.DictReader(survey_file)
	for row in reader:
		survey_dict.append(row)

with open("survey.csv") as survey_file:
	fieldnames = ['email', 'twitter', 'github']
	reader = csv.DictReader(survey_file)
	for row in reader:
		survey_emails.append(row['email'])



#for entry in survey_dict:
#	survey_emails.append(survey_dict[:]['email'])

#print survey_dict
#for index,row in enumerate(survey_dict):
#	if row['email'] == 'beyonce@beyonce.com':
#		print row