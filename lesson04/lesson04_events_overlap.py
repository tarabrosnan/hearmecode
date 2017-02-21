# Goal 2: Who came to *both* your Film Screening and your Happy hour?

def overlap(file1, file2):

	with open(file1, 'r') as file1:
		file1_contents = file1.read().split('\n')

	with open(file2, 'r') as file2:
		file2_contents = file2.read().split('\n')

	overlap = []

	for entry in file1_contents:
		if entry in file2_contents:
			overlap.append(entry)

	return overlap

print overlap("film_screening_attendees.txt", "happy_hour_attendees.txt")