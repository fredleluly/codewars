import re
def body_count(code):
    #your code here
#     CN_pattern = re.search(r'\w',code)
    CN_pattern = re.search(r'([A-Z]\d)(\w\d)(\w\d)(\w\d)([a-zA-Z]\d)\.\-\w%\d\.\d\d\.',code)
    try:
        print(CN_pattern.group())
        if CN_pattern.group() :
            print("okay ")
            return True
    except:
        return False
#print(solve())
#print(body_count())


print(body_count('A6C2E5Z9A4.-F%8.08.'), True)
print(body_count('PP P6A6T5F5S3.-Z%1.11.hgr'), True)
print(body_count('A6A1E3A8M2.-Q%8.88.'), True)
print(body_count('d G8H1E2O9N3.-W%8.56. f'), True)
print(body_count('B4A1D1I8B4.-E%8.76.'), True)
print(body_count('ffr65A C8K4D9U7V5.-Y%8.00.'), True)
print(body_count(' 76     B2L4D0A8C6.-T%8.90.       lkd'), True)
print(body_count('B2L4D0A8C6.-T%8.90'), False)
print(body_count('B2L4D0AFC6.-T%8.90.'), False)
print(body_count('B4A1D1I8B4'), False)
print(body_count('B4A6666...'), False)
print(body_count('B4A1D1I000.-E%0.00.)'), False)
print(body_count('.-E%8.76.'), False)
print(body_count('B4A1t6I7.-E%8.76.'), False)
print(body_count('b4A1D1I8B4.-E%8.76.'), False)
