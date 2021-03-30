def namelist(names):
    if names:
        if len(names) == 1:
#             print(names,len(names))
            return names[0]['name']
        elif len(names) == 2:
#             print(names,len(names))
            return "{} & {}".format(*[str(list(i.values())[0]) for i in names])
        else:
#             print(names[-1])
            back = list(names[-1].values())[0]
            names = names[:-1]
            return "{} & {}".format(', '.join([*[str(list(i.values())[0]) for i in names]]),back)
            
#         if len(names) == 1: return names.values()
#     return f"{}"
    else: return ''
print("Basic tests")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), '| ==> Bart, Lisa, Maggie, Homer & Marge',
    "Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), '| ==> Bart, Lisa & Maggie',
    "Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), '| ==> Bart & Lisa', 
    "Must work with two names")
print(namelist([{'name': 'Bart'}]), '| ==> Bart', "Wrong output for a single name")
print(namelist([]), '', "Must work with no names")