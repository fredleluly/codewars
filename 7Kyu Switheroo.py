def switcheeroo(string):
    returned = ''
    for i in string:
        if i == 'a':
            returned += 'b'
            continue
        if i == 'b':
            returned += 'a'
            continue
        returned += i
    return returned
def switcheeroo(string):
    returned = string.replace('a','|').replace('b','a').replace('|','b')
#     returned = returned.replace('b','a')
    return(returned)
print(switcheeroo("abc"))
print(switcheeroo('aaabcccbaaa'))
print(switcheeroo('ccccc'))
print(switcheeroo('abababababababab'), 'babababababababa')
print(switcheeroo('aaaaa'), 'bbbbb')
