def index_of(words,target):
    #print(words,target)
    adagak = filter(lambda a: target in a,words)
    print("filter",list(adagak))
    returned = None
    for index,i in enumerate(words):
        if target in i:
            return index 
#print(solve())
print(index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'], 'codewars'), 7)
print(index_of(['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj'], 'akC'), 9)
