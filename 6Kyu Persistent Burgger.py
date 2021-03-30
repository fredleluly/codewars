def persistence(n):
	result = n
	if len(str(n)) == 1 : return 0
	many = 0
	while len(str(result)) > 1:
		temp = 1
		for i in [int(i) for i in list(str(result))]:
			temp = temp * i
		result = temp
		many += 1
	return(many)

# little refactor

def persistence(n):
	if len(str(n)) == 1 : return 0
	many = 0
	while len(str(n)) > 1:
		temp = 1
		for i in [int(i) for i in list(str(n))]:
			temp = temp * i
		n = temp
		many += 1
	return(many)

print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)