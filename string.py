
##string=''' reva devu revanth
##prasad le daa'''
##
##ans=[]
##for i in string:
##    if i == '0':
##        ans.append(i)
##print(len(ans))
###print(string.count(' '))

##string=input()
##
##ans=[]
##for i in string:
##    if i in 'AEIOUaeiou':
##        ans.append(i)
##print(*ans)
##
##ans=[]
##print(len(ans))
##
##string="a b c d e f g h i j k l m n o p q r s t u v w x y z"
##print(string.count(' '))
##
##ans=[i for i in string if i in 'AEIOUaeiou' ]
##print(ans)

##inp=input()
##ans=[i for i in inp if i in '0123456789' ]
##print(*ans)


##lst=[]
##inp=input()
##for i in inp:
##    if i not in 'AEIOUaeiou':
##        lst.append(i)
##print(*lst)
string=input()

lst=[i for i in string if i not in 'AEIOUaeiou' ]
print(lst)

