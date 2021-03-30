import re
def bears(x,s):
    #your code here
    bears = (re.findall(r'(8B|B8)',s))
    female = re.findall(r'(B8|8B)',s)
    countMale = re.findall('B',s)
    countFemale = re.findall('8',s)
    print(len(bears),x)
    mating_pairs = len(bears)%3
    print()
    
    
#     if len(bears) == 0 and x == 0:
#         return ['',True]
#     if len(bears) == 0 :
#         return ['',False]
    return([''.join(bears),True if len(''.join(bears)) >=x or x ==0 else False])


#     if len(bears) >= x or x ==0:
#         return [''.join(bears),True]
#     if mating_pairs >= x or x == 0:
#         return [''.join(bears),True]
#     return [''.join(bears),False]
    
    
#     print(s,"\n",bears,len(countMale),"\n",female,len(countFemale),"\n",x)
    
    
    
#     print(x)
#print(solve())
print(bears(7, '8j8mBliB8gimjB8B8jlB'))
print(bears(3, '88Bifk8hB8BB8BBBB888chl8BhBfd'))
print(bears(12,'BgBBBkBcBBkBBBBl8h8BbB8'))
