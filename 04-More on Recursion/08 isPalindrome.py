
def isPalindrome(strn):
    if len(strn)==0:
        return True
    if strn[0]!=strn[len(strn)-1]:
        return False
    return isPalindrome(strn[1:-1])

print(isPalindrome("ioioi"))