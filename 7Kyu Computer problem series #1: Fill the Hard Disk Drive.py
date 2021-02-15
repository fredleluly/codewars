def save(sizes, hd): 
    # your code here
    output = 0
    for i in range(len(sizes)):
#        print(sum(sizes[:i+1]))
        if sum(sizes[:i+1]) == hd or sum(sizes[:i+1]) <= hd:
            output = i+1
    return(output)
    if len(sizes) == 1:
        if sizes[0] > hd:
            return 0
        return 1 
    if output == 0 :return 0
    return None
print("solve()")
print(save([4,4,4,3,3], 12), 3)
print(save([4,4,4,3,3], 11), 2)
print(save([4,8,15,16,23,42], 108), 6)
print(save([13], 13), 1)
print(save([1,2,3,4], 250), 4)
print(save([100], 500), 1)
print(save([11,13,15,17,19], 8), 0)
print(save([45], 12), 0)
