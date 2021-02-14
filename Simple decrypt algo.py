import string
def decrypt(key):
    print(key)
    dict_key = {}
    for i in key:
        if i.isalpha() and i not in dict_key:
            dict_key[i] = 1
        if i.isalpha():

            #print(i)
            dict_key[i] += 1
    #print(dict_key)
    o = ''
    for i in string.ascii_lowercase:
        if i in dict_key:
            o += str(dict_key[i]-1)
            continue
        else:
            o += str(0)
    return(o)
print(decrypt("$aaaa#bbb*ccfff!z"))
print(decrypt("z$aaa#ccc%eee1234567890"))
#print(decrypt("$aaaa#bbb*ccfff!z"))
"""
z$aaa#ccc%eee1234567890
"""
