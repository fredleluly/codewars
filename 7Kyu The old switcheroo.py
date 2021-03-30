import re
def vowel_2_index(string):
    #your code here
#     returned = re.sub(r'([aeiou])',str(ord(r'\1')),string)
    returned = ''
    for index,i in enumerate(string):
        returned += re.sub(r'([aeiouAEIOU])',str(index+1),i)
    return returned
    # no no no not good i like to readable code 
    #return ''.join([re.sub(r'([aeiouAEIOU])',str(index+1),i) for index,i in enumerate(string)])
#print(solve())
print(vowel_2_index('Kakek tomoro Tomorrow is going to be raining'),'T2m4rr7w 10s g1415ng t20 b23 r2627n29ng')
