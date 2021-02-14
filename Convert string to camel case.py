import re
def to_camel_case(text):
    words = [i[0].upper() + i[1:] for i in re.split('[-_]',text)]
    #print(words)
    if text[0] == text[0].lower():
        words[0] = words[0].lower()
        print(words[0])
    return ''.join(words)
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))
"""

the-Stealth-Warrior
-



"""
