# Find gcd(greatest common divisor) of 2 no.s using recursion

def gcd(max,min):
    assert int(max)==max and int(min)==min,"Both of them should be integers"
    if(max<0 or min<0):
        max=max*-1
        min=min*-1
    if(min==0):
        return max
    else:
        return gcd(min,max%min)
    
print(gcd(-10,-5))