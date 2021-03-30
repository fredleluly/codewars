def digital_root(n):
    num = str(n)
    while len(num) > 1:
        num = str(sum(map(int,num)))
    return int(num)
print(digital_root(3334445558224416662255))

