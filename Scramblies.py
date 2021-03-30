import numpy as np
def scramble(s1,s2):
    #print(y)
    
    y = np.array([ord(i) for i in s2])
    x = np.array([ord(i) for i in s1])
    #print(x[ord])
    pa2 = 0
    for i in y:
        #pass
        z2 = np.count_nonzero(y == i)
        z1 = np.count_nonzero(x == i)
        #print(z2)
        #pass
        #z2 = x.count(i)
        #z1 = x.count(i)
        if z1 == z2 or z1 >= z2:
            pa2 +=1

    if pa2 == len(s2): return True
    print("pa : ",pa2)
    f1 = list(s1)
    o = []
    pa = 0
    #slow = [s1.count(i) == s2.count(i) for i in list(s2)]
    #print(slow == len(s2))
    #for i in list(s2):
    #    x = s1.count(i)
    #    z = s2.count(i)
    #
    #    if x == z or x >= z:
    #        pa += 1
    #if pa == len(s2):
    #    print('yey')
    #else:
    #    print('why')
    #print(pa)
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('rkqodlw', 'world'))
"""
"""
