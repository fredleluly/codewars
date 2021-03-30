def lovefunc( flower1, flower2 ):
    if flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    elif flower2 % 2 != 0 and flower1 % 2 == 0:
        return True
    return False

print(lovefunc(1,4), True)
print(lovefunc(2,2), False)
print(lovefunc(0,1), True)
print(lovefunc(0,0), False)