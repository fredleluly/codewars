def solve(s,n):
    o = []
    sort_s = sorted(s)
    temp = s[0]
    for i in range(n):
        if temp < s[i]:
            #print(s[0])
            temp = s[i]
        #o.append(sort_s[i])
    print(temp," : ")
print(solve([1,2,3,4,1],3))
