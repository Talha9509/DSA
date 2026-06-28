
def reverse(strn):
    if len(strn)<=0:
        return strn
    return strn[len(strn)-1]+reverse(strn[0:len(strn)-1])

print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'