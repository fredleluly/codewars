def capitalize(s):
    returnedOdd = ''
    returnedEven = ''
    for index,i in enumerate(s):
        if index % 2 == 0:
            returnedEven += i.upper()
            returnedOdd += i.lower()
        else:
            returnedEven += i.lower()
            returnedOdd += i.upper()
    return [returnedEven,returnedOdd]
            
print(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
print(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])            
