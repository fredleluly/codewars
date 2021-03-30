def solve(s):
    tmap = [
[ 8, 4, 2, 9, 9, 4, 5, 6,10, 9], 
                            [ 3, 3, 6, 9, 7, 7, 5, 7, 7, 3], 
                            [ 0, 9, 8, 5, 5, 8, 0, 3, 9, 2], 
                            [ 1, 2, 8, 0, 0, 2, 9, 4, 7, 3], 
                            [10, 4, 7, 2, 6, 2,10,10, 9, 5], 
                            [ 3, 0, 4, 0, 5, 5, 2, 4, 6, 7], 
                            [ 0, 9, 2, 1, 4, 4, 1, 1, 8, 6], 
                            [ 0, 6, 7,10, 9, 1, 6, 7, 3, 8], 
                            [ 4, 7,10, 4, 1, 4, 10,6, 8, 7], 
                            [ 8, 0, 5, 0, 7, 6, 0, 1, 6, 3]
            ]

#    for i in range(len(tmap)):
#        for ele in range(1,len(tmap)):
#*            if tmap[ele-1][i] + tmap[ele][i] == s:
#*                #print('doule s',tmap[ele-1][i],tmap[ele][i])
#*                print(ele-1,i,"*",ele,i)
#            if tmap[i][ele-1] + tmap[i][ele] == s:
#                #print("s",tmap[i][ele-1],tmap[i][ele])
#                print(i,ele-1,"|",i,ele)
#            if tmap[ele-1][i] + tmap[ele][i] == s:
#                #print('doule s',tmap[ele-1][i],tmap[ele][i])
#                print(ele-1,i,"*",ele,i)
    print("="*20)
    for i in range(len(tmap)):
         for ele in range(len(tmap)):
             for setiap in range(len())

#print(solve(3))
print(solve(9))
