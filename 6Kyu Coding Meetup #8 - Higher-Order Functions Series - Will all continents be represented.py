def all_continents(lst): 
    count = 0
#     print(lst[:]['continent'])
    lst = [lst[i]['continent'] for i in range(len(lst))]
    lists_continents =  ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    if lst.count(lists_continents[0]):
        count += 1
    if lst.count(lists_continents[1]):
        count += 1
    if lst.count(lists_continents[2]):
        count += 1
    if lst.count(lists_continents[3]):
        count += 1
    if lst.count(lists_continents[4]):
        count += 1
    return True if count >= 5 else False

# refactoring
def all_continents(lst): 
    lst = [lst[i]['continent'] for i in range(len(lst))]
    lists_continents =  ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    return all(lst.count(lists_continents[i]) != 0 for i in range(len(lists_continents)))
