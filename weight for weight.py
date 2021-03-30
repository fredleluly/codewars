def sortbydigit(inputs):
    numList = sorted(inputs.split())
    #print(sum(list(numList[0])))
    print()
    sores = False
    temp = 0
    while not sores:
        sores = True
        for i in range(len(numList)-1):
            #print(numList[i],numList[j])
            # countings
            if sum([int(ik) for ik in  list(numList[i])])> sum([int(ik) for ik in  list(numList[i+1])]):
            #if numList[i] > numList[i+1]:
                temp = numList[i]
                numList[i] = numList[i+1]
                numList[i+1] = temp
                sores = False
    return numList
print(sortbydigit("56 65 74 100 99 68 86 180 90"))
