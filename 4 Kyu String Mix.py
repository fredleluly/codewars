# test
def solve(s1,s2):
    output1 = {}
    output2 = {}
    for i in s1:
        #should = s1.count
        if s1.count(i) >= 1 and s2.count(i) >= 1 and i.isalpha():
            output1[i] = s1.count(i)
            output2[i] = s2.count(i)
    thereal = {}
    for i in output1:
        thereal[i] = output1[i] if output1[i] > output2[i] else output2[i]
    returned = ''
    pip = {k: v for k, v in sorted(thereal.items(), key=lambda item: item[1]) if v != 1}
    print(pip)
    # for i in reversed(pip):
        # print(i)
    # for i in reversed(pip):
        # if output1[i] == pip[i]:
        #     returned += '1:{}/'.format("".join([pip. for i in range(pip[i])]))
        # if output2[i] == pip[i]:
        #     returned += '2:{}/'.format("".join([pip. for i in range(pip[i])]))


        # returned += i

    # for k,v in list(sorted(pip.items(), key = lambda i : (i[1],i[0]), reverse = True)):
    #     if output1[k] == output2[k]:
    #         returned += '=:{}/'.format("".join([k for i in range(v)]))
    #         continue
    #     if output1[k] == v:
    #         returned += '1:{}/'.format("".join([k for i in range(v)]))
    #     if output2[k] == v:
    #         returned += '2:{}/'.format("".join([k for i in range(v)]))
    # print(returned)


    # print('the real',sorted(thereal))
    # therealtemo = dict(sorted(thereal.items(), key=lambda item: item[0]))
    # #print(therealtemo)
    # pip = {k: v for k, v in sorted(therealtemo.items(), key=lambda item: item[1])}
    # for i in reversed(pip):
    #     print(i)
    returned = []
    # pip.reverse()
    for i in reversed(pip):
        if output1[i] == output2[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i
            returned.append("=:"+str(jumlah)+"/")
            continue
        if output1[i] == pip[i]:
            # print("output1")
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("1:"+str(jumlah)+"/")
        if output2[i] == pip[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("2:"+str(jumlah)+"/")

    b_list = sorted(returned, key=str.lower)
    b_list.sort(key=len, reverse=True)
    print(b_list)
# print(solve("my&friend&Paul has heavy hats! &","my friend John has many many friends &"))

# print(solve("mmmmm m nnnnn y&friend&Paul has heavy hats! &","my frie n d Joh n has ma n y ma n y frie n ds n&"))
# print(solve("Are the kids at home? aaaaa fffff","Yes they are here! aaaaa fffff"))
"""
Are the kids at home? aaaaa fffff
Yes they are here! aaaaa fffff
"""
# def mix(s1, s2):
def mix(s1,s2):
    output1 = {}
    output2 = {}
#     print(s1,"\n",s2)
    s1 = s1
    s2 = s2
    res = []
    res = [] 
    [res.append(x) for x in s1 if x not in res] 
    [res.append(x) for x in s2 if x not in res] 
#     print(res.count('s'),s1.count('s'))
    for i in res:
        if i.isalpha() and i.islower():
            output1[i] = s1.count(i)
            output2[i] = s2.count(i)

    thereal = {}
    for i in output1:
        thereal[i] = output1[i] if output1[i] > output2[i] else output2[i]
    returned = ''
    pip = {k: v for k, v in sorted(thereal.items(), key=lambda item: item[1]) if v != 0 and v!=1}
#     print(pip)
#     for k,v in sorted(thereal.items(), key=lambda item: item[1]):
#         if v != 0 and v != 1:
            
    returned = []
    for i in list(reversed(sorted(pip.keys()))):
#         print(i)
        if output1[i] == output2[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i
            returned.append("=:"+str(jumlah)+"/")
            continue
        if output1[i] == pip[i]:
            # print("output1")
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("1:"+str(jumlah)+"/")
        if output2[i] == pip[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("2:"+str(jumlah)+"/")

    b_list = sorted(returned, key=str.lower)
    b_list.sort(key=len, reverse=True)
#     print(b_list)
    return(''.join(b_list)[:-1])
print(mix("my&friend&Paul has heavy hats! &","my friend John has many many friends &"))

print(mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &","my frie n d Joh n has ma n y ma n y frie n ds n&"))
print(mix("Are the kids at home? aaaaa fffff","Yes they are here! aaaaa fffff"))

# def mix(s1, s2):
def mix(s1,s2):
    output1 = {}
    output2 = {}
    s1 = s1
    s2 = s2
    res = []
    [res.append(x) for x in s1 if x not in res] 
    [res.append(x) for x in s2 if x not in res] 
    for i in res:
        if i.isalpha() and i.islower():
            output1[i] = s1.count(i)
            output2[i] = s2.count(i)
    thereal = {}
    for i in output1:
        thereal[i] = output1[i] if output1[i] > output2[i] else output2[i]
    returned = ''
    pip = {k: v for k, v in sorted(thereal.items(), key=lambda item: item[1]) if v != 0 and v!=1}
    returned = []
    for i in list(reversed(sorted(pip.keys()))):
        if output1[i] == output2[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i
            returned.append("=:"+str(jumlah)+"/")
            continue
        if output1[i] == pip[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("1:"+str(jumlah)+"/")
        if output2[i] == pip[i]:
            jumlah = ''
            for ch in range(pip[i]):
                jumlah+= i 
            returned.append("2:"+str(jumlah)+"/")
    b_list = sorted(returned, key=str.lower)
    b_list.sort(key=len, reverse=True)
    return(''.join(b_list)[:-1])
