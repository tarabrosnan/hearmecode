def textfile_to_string(filename):

	with open(filename, "r") as text_file:
		text = text_file.read()

	return text

states = textfile_to_string("states.txt")
print states

