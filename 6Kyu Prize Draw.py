from string import ascii_lowercase as asciis
def rank(st, we, n):
    if st == '' : return "No participants"
    if n > len(we): return "Not enough participants"
    realName= st.split(',')
    stModif = list(map(lambda w: {w:(sum([asciis.index(i.lower())+1 for i in w]) + len(w))*we[realName.index(w)]},realName))
    print(stModif)
    def keys(arr):
        return list(arr.values())[0]
    stModif.sort(key=lambda x: list(x.keys())[0])
    stModif.sort(key=keys,reverse=True)
    return(list(stModif[n-1].keys())[0])