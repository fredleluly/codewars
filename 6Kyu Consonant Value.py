def solve(s):
    value = 0
    for i in s:
        if i.lower() not in "aeiou":
            value += ord(i) -98
            print(i)
    print(value)
    return sum([ord(i) -98 for i in s if i.lower() not in "aeiou"])
def solve(s):
    import re
    sperate_s = re.split("a|e|i|o|u",s)
    print(sperate_s)
    o = []
    for i in sperate_s:
        print(i)
#         if i :
        o.append(sum([ord(c)-96 for c in i]))
    print(o)
    return max(o)
#     return sum([int(ord(i)) -95  for i in sperate_s if i != ''])
print(solve("zodiac"),26)
