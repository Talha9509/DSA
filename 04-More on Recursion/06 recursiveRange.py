# range of no.s when added till n from 0 (from 0 to any no. is no. only so not takong 0)

def recRange(n):
    if(n<=0):
        return 0
    return n+recRange(n-1)

print(recRange(10))