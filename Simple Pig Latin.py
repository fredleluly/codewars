def pig_it(tex):
	special_characters = "@#$%^&*()-+?_=,<>/!"
	newa = tex.split()
	allw = ''
	for i in newa:
		# print(i[1:])
		if i in special_characters:
			allw += i + ' '
			continue
		# if len(i) == 1:
		# 	allw += i + ' '
		# 	continue
		allw += i[1:] + i[0] + 'ay '
	# return allw[:-1] == 'igPay atinlay siay oolcay'
	return allw[:-1]
	print(allw)
print(pig_it('O tempora o mores !'))  
print(pig_it('eniVay idivay icivay'))  
"""
eniVay idivay icivay
"""