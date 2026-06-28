# Convert decimal to binary no.

def dtob(n):
    assert int(n)==n,"it must be integer"
    if n==0:
        return 0
    else:
        return ((n%2)+(10*dtob(int(n/2))))
        # return ((n%2)+(10*dtob(n//2)))  is not correct for negative no.s because when it reaches -1//2 then it is -1 but not 1

print(dtob(-17))