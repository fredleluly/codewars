def find_it(seq):
    o = []
    for i in seq:
        c = 0
        for i2 in seq:
            if i == i2:
                c += 1
        #print(i)
        if c % 2 == 0:
            pass
        else:
            return i
print(find_it([2,2,2,2,2,2,2,2,1]))
