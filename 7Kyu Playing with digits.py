def solve(s,k):
    lstr = str(s)
    return_sum = 0
    temp_k = k
    ab = []
    for i in lstr:
        return_sum += pow(int(i),temp_k)
        temp_k += 1
        ab.append(i)
    #print(f'{return_sum//s} since {''.join(ab)} = {return_sum} = {s} * since')
    print(return_sum,s)
    print(return_sum//s)
    
print(solve(46288,3))

print(solve(46288,5))
