def count_salutes(hallway):
    hallway = hallway.replace('-','')
    length = len(hallway)
    count = 0
    for i in range(length):
        if hallway[i] == '>':
            count += hallway[i:].count('<')
        elif hallway[i] == '<':
            count += hallway[:i].count('>')            
    return(count)
            
print(count_salutes('<---->---<---<-->'), 4)
print(count_salutes('------'), 0)
print(count_salutes('>>>>>>>>>>>>>>>>>>>>>----<->'), 42)
print(count_salutes('<<----<>---<'),2)
print(count_salutes('>'),0)