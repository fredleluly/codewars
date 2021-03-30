"""
/ "The more we witness our          \
| emotional reactions and understand how |
| they work, the easier it is to         |
| refrain."                           |
|                                        |
\ --Pema Chodron               /
 ----------------------------------------
 """
import re
def solution(string,markers):
    update_string = ''
    # print(string,markers,"\n====")
    for i in markers:
        ada = re.search(fr" ?\{i}.*",string)
        if ada:
#             print(ada.group())
            string = re.sub(fr" ?\{i}.*",'',string)
    # print(f"====\n{string}")
    return(string)
# 'apples, pears\ngrapes\nbananas'
import re
def solution(string,markers):
    for i in markers:
        string = re.sub(fr" ?\{i}.*",'',string)
    return(string)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
