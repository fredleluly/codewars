def to_weird_case(string):
    returned = []
    for i in string.split():
        temp = ''
        for index,c in enumerate(i):
            if index % 2 == 0:
                temp+= c.upper()
            else:
                temp+= c.lower()
        returned.append(temp)
    return(' '.join(returned))
