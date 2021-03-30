def dup(arry):
    returned = []
    for i in arry:
#         returned.append(''.join([c for index,c in enumerate(i) if c not in i[:index]]))
        temp = ''
        for c in range(len(i)-1):
            if (c) == len(i)-1:
                print(i[c])
            if i[c] == i[c+1]:
                continue
            temp+= i[c]
        returned.append(temp+i[-1])
    # should be wrong the test not explicits
    return(returned)
print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo'])
print(dup(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese'])
print(dup(["kelless","keenness"]), ['keles','kenes'])
print(dup(["Woolloomooloo","flooddoorroommoonlighters","chuchchi"]), ['Wolomolo','flodoromonlighters','chuchchi'])
print(dup(["adanac","soonness","toolless","ppellee"]), ['adanac','sones','toles','pele'])
print(dup(["callalloo","feelless","heelless"]), ['calalo','feles','heles'])
print(dup(["putteellinen","keenness"]), ['putelinen','kenes'])
print(dup(["kelless","voorraaddoosspullen","achcha"]), ['keles','voradospulen','achcha'])
