def spoonerize(words):
	returned = []
	splitedWords = words.split()
	for i in range(len(splitedWords)):
		coba = ''
		if i == 0 :
			print(i)
			coba = splitedWords[i+1][0] 
		else:
			print("else",i)
			coba = words[0]
		splitedWords[i] = coba + splitedWords[i][1:]
	return splitedWords
# sorry to tryin to hard my bad
print(spoonerize("nit picking"), "pit nicking")
print(spoonerize("wedding bells"), "bedding wells")
print(spoonerize("jelly beans"), "belly jeans")
print(spoonerize("pop corn"), "cop porn")