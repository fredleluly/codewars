def order(sentence):
    resArr = sentence.split()
    result = {}
    for i in resArr:
        for j in i:
            if j.isdigit():
                result[j] = i
    # print(sorted(result))
    return ' '.join(dict(sorted(result.items())).values())
    # return 0
print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")