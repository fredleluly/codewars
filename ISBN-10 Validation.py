import re
def validation(isbn):
    reisbn = re.search('^[0-9]{9}[0-9]$',str(isbn))
    lenisbn = len(str(isbn))
    strisbn = str(isbn)
    ot = []
    if reisbn:
        for i in range(lenisbn):
            print(i+1)
            ot.append(int(strisbn[i])*(i+1))
        ot2 = sum(ot) % 11
    print(ot2)
    return True if reisbn and not ot2 else False
print(validation(1112223339))
