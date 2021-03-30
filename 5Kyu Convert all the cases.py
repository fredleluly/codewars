import re
from string import ascii_uppercase as up
def change_case(identifier, targetCase):
    print(identifier,targetCase)
    
    if identifier.__contains__('-') + identifier.__contains__('_') + bool(identifier != identifier.lower()) > 1:
        return None
    
    # kebab
    if targetCase == 'kebab':
        return re.sub(r"([A-Z])",r"-\1",identifier).lower().replace('_','-')
    # camel
    if targetCase == 'snake':
        return re.sub(r"([A-Z])",r"_\1",identifier).lower().replace('-','_')        
    # snake
    if targetCase == 'camel':
        return re.sub(r"([_-])(\w)",lambda match_object: match_object.group(2).upper() ,identifier)
    
#     if identifier == '': return ''
#     apa = ''
#     olehGak = any(x.isupper() for x in identifier)
#     if '-' in identifier and not olehGak and '_' not in identifier:
#         catch = identifier.split('-')
#         apa += 'dash'
# #         print(catch)
#     elif '_' in identifier and not olehGak and '-' not in identifier:
#         catch = identifier.split('_')
#         apa += 'underScore'
#     elif olehGak and '_-' not in identifier:
#         catch = re.findall('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
#         apa += 'camel'
#     else:
#         return None    
#     for i in ''.join(catch):
#         if i =='-' or i == '_':
#             return None
#     catch = [i.lower() for i in catch]
#     if targetCase == 'snake':
#         result = '_'.join(catch)
#     elif targetCase == 'kebab':
#         result = '-'.join(catch)
#     elif targetCase == 'camel':
#         result = ''.join([catch[0]+''.join([i.title() for i in catch[1:]])])
#     else:
#         return None
#     print(result)
#     return(result)

print(change_case("snakeCase", "snake"), "snake_case", "camelCase to snake_case conversion should work")
print(change_case("some-lisp-name", "camel"), "someLispName", "kebab-case to camelCase conversion should work")
print(change_case("map_to_all", "kebab"), "map-to-all", "snake_case to kebab-case conversion should work")
print(change_case("doHTMLRequest", "kebab"), "do-h-t-m-l-request", "camelCase to kebab-case conversion should work")
print(change_case("invalid-inPut_bad", "kebab"), None, "mIx-ed_cAse input should be considered invalid")
print(change_case("valid-input", "huh???"), None, "Invalid target cases should be dealt with")
print(change_case("", "camel"), "", "An empty string should not be changed.")
