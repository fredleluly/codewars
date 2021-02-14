def decrypt(input):
    return ''.join(["'"+str(ord(i))+"'" if i != ' ' and not i.isdigit() else i for i in reversed(input)])
print(decrypt("9Hi Alice4"))
