def find_uniq(arr):
    # your code here
    nux = {}
    unix = []
    for i in arr:
    	if i not in nux:
    		nux[i] = 1
    	else:
    		nux[i] +=1
    for j in nux:
    	if nux[j] < 2:
    		return j
	# if len(nux[i]) < 2:
	# 	unix.append(nux[i])

    # return (i for i in nux if i not in unix)   # n: unique integer in the array
    # return nux.items()




print(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
print(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
print(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
