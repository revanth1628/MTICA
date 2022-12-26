def extract_digit(s):
    temp_vowel=''
    for i in s:
        #print("i=",i)
        if i in '123456789':
            temp_vowel+=i
            #print("i",i"temp_vowel:",temp_vowel)
    return temp_digit
#str1=input("enter the string:")    
str1=input()
a=extract_digit(str1)
print("digit:",a)
