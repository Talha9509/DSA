
def flatten(listt):
    result=[]
    for i in listt:
        if type(i) is int:
            result.append(i)
        elif type(i) is list:
            result=result+flatten(i)
    return result

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]