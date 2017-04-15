# The function takes a sentence as an argument so it can scan it
def scan(word):
	# See if the word is a direction
	# If the word is a direction, pair it up with the direction type
	# Else, move on
	direction = ['north', 'west', 'south', 'east']

	if word in direction:
		return [('direction', word)]