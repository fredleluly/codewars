def bolehGak(recipe,available):
    haved = 0
    for i in recipe:
        try:
            if available[i] and recipe[i]:
                if available[i]-recipe[i] >= 0:
                    haved += 1
        except:
            pass
    return True if haved == len(recipe) else False

def cakes(recipe, available):    
    many = 0
    boleh = bolehGak(recipe,available)
    while boleh:
        for j in recipe:
            available[j] = available[j] - recipe[j] 
        many += 1
        boleh = bolehGak(recipe,available)
    return many
print(cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}),2)
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000, "milk": 2000}),0)
