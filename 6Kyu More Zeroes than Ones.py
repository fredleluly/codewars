def more_zeros(s):
    returned = []
    res = []
    [res.append(i) for i in list(s) if i not in res]
    for i in res:
#         print(('{:b}'.format(ord(i)).count('0')))
        if ('{:b}'.format(ord(i)).count('0')) > ('{:b}'.format(ord(i)).count('1')):
            returned.append(i)
    return(returned)
print(more_zeros('abcde'), ['a', 'b', 'd'])
print(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
print(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
print(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'), ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0'])
print(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])
