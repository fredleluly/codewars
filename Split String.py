def solution(s):
    o = []
    print(len(s))
        
    for i in range(int(len(s)/2)):
        print(i)
        o.append(s[i]+s[i+1])
    if type(len(s)/2) == float:
        o.append(s[-1]+ '_')
    print(o)
print(solution('abcde'))
