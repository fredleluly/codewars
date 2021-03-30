def name_value(my_list):
    o = None
#     for element in my_list:
#         for i in element:
    o = ([sum([(ord(i) - 96)for i in element if i != ' '])*(index+1) for index,element in enumerate(my_list)])
    return o
#     return_element = []
#     for index,i in enumerate(o): 
#         return_element.append(i*index+1)
#         print(i*(index+1))
#         pass
print(name_value(["codewars","abc","xyz"]))
