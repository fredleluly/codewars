def fold_array(array, runs):
    import copy
    notMy = []
    for run in range(runs):        
        sumsk = copy.deepcopy(array)
        sums = []
        if run > 0 :
            sumsk = copy.deepcopy(notMy)
        if len(sumsk) % 2 == 0:
            for i in range(len(sumsk)//2):
                sums.append(sumsk[i] + sumsk[-1+-i])
            # pass
        else:
            # print(len(sumsk)//2)
            # print(sumsk[len(sumsk)//2])
            for i in range(len(sumsk)//2):
                sums.append(sumsk[i] + sumsk[-i+-1])
            sums.append(sumsk[len(sumsk)//2])
        notMy = copy.deepcopy(sums)
    print(notMy)
    return notMy
print(fold_array([1, 2, 3, 4, 5],2))
print(fold_array([-9, 9, -8, 8, 66, 23],1))

"""
-9, 9, -8, 8, 66, 23
"""