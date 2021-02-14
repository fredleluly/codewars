def play_pass(s, n):
    # your code
    import string
    o = ''
#     print(string.ascii_uppercase)
    
    for index,i in enumerate(s):
#         print(i)
        if i.isalpha():
            if index%2 != 0:
                o += string.ascii_lowercase[(string.ascii_uppercase.index(i)+n)%len(string.ascii_uppercase)]
            else:
                o += string.ascii_uppercase[(string.ascii_uppercase.index(i)+n)%len(string.ascii_uppercase)]
        if i.isdigit():
            o += str(9 - int(i))
        else:
            if not i.isalpha():
                o += i
    return ''.join(reversed(o))
