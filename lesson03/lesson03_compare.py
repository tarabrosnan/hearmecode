# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.
with open("all_employees.csv", "r") as employee_file:
	employees = employee_file.read().split("\n")

with open("survey.csv", "r") as survey_file:
	survey = survey_file.read().split("\n")

employee_emails = []
survey_emails = []

for index, employee in enumerate(employees):
	employees[index] = employees[index].split(", ")
	employee_emails.append(employees[index][1])

for index, entry in enumerate(survey):
	survey[index] = survey[index].split(",")
	survey_emails.append(survey[index][0])

employee_emails.pop(0)
survey_emails.pop(0)
#print employee_emails
#print survey_emails

for email in survey_emails:
	if email in employee_emails:
		print email

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github




