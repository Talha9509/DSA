# Sum of Digits of positive integer using recursion

# def dividebyTen(n):
#         # pass
#         tens=n//10
#         ones=n%10
#         return tens,ones
# def Sum(a):
#     if (a==0):
#         return 0
#     else:
#         tens,ones= dividebyTen(a)
#         if tens>=10:
#             tens, ones = dividebyTen(tens)
#         return ones+Sum(tens)
    
# print(Sum(59))


def SumofDigits(n):
    assert n>=0 and int(n)==n,""
    if n==0:
        return 0
    else:
        return int(n%10)+SumofDigits(int(n/10))

print(SumofDigits(112))