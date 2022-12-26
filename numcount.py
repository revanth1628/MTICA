##def vowelcount(s):
##    vowel=0
##    for i in s:
##        if i in 'AEIOUaeiou':
##            vowel+=1
##    return vowel
##str1=input()
##a=vowelcount(str1)
##print("no of vowels in a'",str1,"'is",a)
##               

##def concount(s):
##    con=0
##    for i in s:
##        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
##            con+=1
##    return con
##str1=input()
##a=concount(str1)
##print("no of consonantcount in a'",str1,"'is",a)
##
def numcount(s):
    num=0
    for i in s:
        if i in '0123456789':
            num+=1
    return num
str1=input()
a=numcount(str1)
print("no of number count in a'",str1,"'is",a)
               
