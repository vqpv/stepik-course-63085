phrase = 'Take only the words that start with t in this sentence'

print([i for i in phrase.split() if i[0].lower() == 't'])
