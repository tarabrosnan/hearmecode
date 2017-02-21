with open("all_employees.csv") as employees_file:
	employees = employees_file.read().strip().split('\n')

for index, row in enumerate(employees):
	employees[index] = employees[index].split(',')

header = employees.pop(0)
print header
print employees