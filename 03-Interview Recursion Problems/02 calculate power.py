# calculate the power of number using recursion

def powerofNum(base,exp):
    assert exp>=0 and int(exp)==exp,"Exponential must be positive integer"
    if(exp==0):
        return 1
    if(exp==1):
        return base
    return base*powerofNum(base,exp-1)

print(powerofNum(3,0))