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

##def numcount(s):
##    num=0
##    for i in s:
##        if i in '0123456789':
##            num+=1
##    return num
##str1=input()
##a=numcount(str1)
##print("no of number count in a'",str1,"'is",a)
##               
##def specialcount(s):
##    special=0
##    for i in s:
##        if i not in 'AEIOUaeiouBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz0123456789':
##            special+=1
##    return special
##str1=input()
##a=specialcount(str1)
##print("no of special count in a'",str1,"'is",a)
##        

def consonant(s):
    temp=''
    for i in s:
        #print("i=",i)
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            temp+=i
            #print("i",i"temp_vowel:",temp_vowel)
    return temp
#str1=input("enter the string:")    
str1=input()
a=consonant(str1)
print(a)
