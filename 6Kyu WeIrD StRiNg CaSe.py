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
print()
print('should return the correct value for a single word')
print(to_weird_case('This'), 'ThIs')
print(to_weird_case('is'), 'Is')

print('should return the correct value for multiple words')
print(to_weird_case('This is a test'), 'ThIs Is A TeSt')
