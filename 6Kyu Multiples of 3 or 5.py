def solution(number):
    o = []
    for i in range(number):
        if i % 3 == 0 or i % 5 ==0:
            o.append(i)
    print(sum(o))
print(solution(10))
