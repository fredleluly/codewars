def array_diff(a, b):
    return [i for i in a if i not in b]

print("Basic Tests")
print(array_diff([1,2], [1]), [2] )
print(array_diff([1,2,2], [1]), [2,2] )
print(array_diff([1,2,2], [2]), [1] )
print(array_diff([1,2,2], []), [1,2,2] )
print(array_diff([], [1,2]), [] )