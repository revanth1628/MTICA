def checkpalindrome(s1):
    if s1==s1[::-1]:
        return 'yes'
    else:
        return 'no'

inp=input()
print(checkpalindrome(inp))

