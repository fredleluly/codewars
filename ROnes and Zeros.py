def binary_array_to_number(arr):
    o = []
    for i,c in enumerate(arr):
        print((len(arr)-1) - i," : ",c)
        #if len(arr) - i == 0:
            #o.append(1)
            #continue
        if arr[(len(arr)-1) - i]:
            o.append(2**(len(arr) -i))
    o2 = [2**i for i,c in enumerate(reversed(arr)) if c]
    print(sum(o))
print(binary_array_to_number([1,0,1,0]))
