import re
def heggeleggleggo(word):
#     pass
    returned = ''
    for i in word:
        if i not in 'aeiouAEIOU':
            returned += re.sub(r'(\w)',r'\1egg',i)
            continue
        returned += i
#             continue
    return(returned)
#print(solve())


print(heggeleggleggo("hello"), "heggeleggleggo")
print(heggeleggleggo("code here"), "ceggodegge heggeregge")
print(heggeleggleggo("FUN KATA"), "FeggUNegg KeggATeggA")
print(heggeleggleggo("egg"), "egegggegg")
print(heggeleggleggo("Hello world"), "Heggeleggleggo weggoreggleggdegg")
print(heggeleggleggo("scrambled eggs"), "seggceggreggameggbeggleggedegg egegggeggsegg")
print(heggeleggleggo("eggy bread"), "egegggeggyegg beggreggeadegg")
