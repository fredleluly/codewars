def solve(s):
    #for i in s:
        #if i.isspace():
    return "".join([i if not i.isupper() else " "+i for i in s])
print(solve("helloWorld"))
