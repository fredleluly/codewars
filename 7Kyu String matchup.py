def solve(a,b):
    o = []
    for i in b:
        o.append(a.count(i))
    print(o)
    return [a.count(i) for i in b]
    return o
print(solve(['abc', 'abc', 'xyz', 'cde', 'uvw'],['abc', 'cde', 'uap']))
