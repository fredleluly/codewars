def binary_array_to_number(arr):
    arr.reverse()
    o = []
    for i,c in enumerate(arr):
        print(i," : ",c)
        if i == 0 and c == 1:
            o.append(1)
            continue
        if c:
            o.append(2**i)
    print(sum(o))
print(binary_array_to_number([1,0,1,0]))
