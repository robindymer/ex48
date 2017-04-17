def scan(sentence):
	# Makes sure that the scan can work on input with caps and input without caps
	sentence = sentence.lower()
	total =[]

	# The dictionary when the statements can check if the word matches any of the types
	directions = ['north', 'west', 'south', 'east']
	verbs = ['go', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'to']
	pronouns = ['her', 'him', 'it']
	nouns = ['bear', 'princess']

	sentence = sentence.split()

	for word in sentence:

		if word in directions:
			total.append(('direction', word))
		elif word in verbs:
			total.append(('verb', word))
		elif word in stops:
			total.append(('stop', word))
		elif word in nouns:
			total.append(('noun', word))
		elif word in pronouns:
			total.append(('pronoun', word))
		elif word.isdigit():
			total.append(('number', int(word)))
		else:
			total.append(('error', word))

	return total

if __name__ == '__main__':
	answer = input('what do you want to do? ')
	print(scan(answer))