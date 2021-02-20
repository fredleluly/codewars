from itertools import permutations
import itertools
def bananas(s):
	items = s
	# print(s)
	# exp = set()
	# for i in s:
	# 	for j in i:
	# 		print(j)
	letters = s
	exp = []
	for n in range(1, len(letters)+1):
		exp.append( list(map(''.join, permutations(letters, n))))
	print([combination for i in range(len(items)+1) for combination in itertools.combinations('bananas', i)])
	# for i in exp:
		# if i == 'bananas':
			# print(i)
	# print(exp)
print(bananas("bbananana"))