# return_list = []
def unpack(list_):
    returned = []
    for element in list_:
        if type(element) == list:
            for i in unpack(element): returned.append(i)
        else:
            returned.append(element)
    return returned 
def flatten(*data):
    return_list = []
    for i in data:
        if type(i) == list:
            for element in unpack(i): return_list.append(element)
        else:
            return_list.append(i)
    return return_list
# don't you ever think to give up
# pam pam pare pam pam pare 
# print(flatten(),[])
print(flatten(1,2,3),[1,2,3])
print(flatten([1,2],[3,4,5],[6,[7],[[8]]]),[1,2,3,4,5,6,7,8])
# print(flatten(1,2,['9',[],[]],None),[1,2,'9',None])
print(flatten(['hello',2,['text',[4,5]]],[[]],'[list]'),['hello',2,'text',4,5,'[list]'])

# print()

