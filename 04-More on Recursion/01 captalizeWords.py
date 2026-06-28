# captalize words

def capWords(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0].upper())
    return result+capWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capWords(words))