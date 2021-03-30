lenisbn = len(str(isbn))
import re
def validation(isbn):
    reisbn = re.search('^[0-9]{9}([0-9]|X)$',str(isbn))
    lenisbn = len(str(isbn))
    strisbn = str(isbn)
    ot = []
    ot2 = True
    print(isbn)
    if reisbn:
#         if 'X'in reisbn.group():
#             print('eo')
        dojo = False
        if '10' in strisbn:
            print('dojo')
            dojo = True
        for i in range(lenisbn):
            #print(i+1)
            ot.append(int(strisbn[i])*(i+1) if strisbn[i] != 'X' else 10*10)
        print(ot)
        ot2 = sum(ot) % 11
        
    
    return True if reisbn and not ot2 else False
print(validation('048665088X'))
