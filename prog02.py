##lst=[]
##for i in range(1,101):
##    if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0 :
##        lst.append(i)
##print(*lst)


##ans=[]
##for i in range(100,111):
##    temp=[]
##    for j in range(1,10):
##        if i%j==0:
##            temp.append(j)
##    ans.append([i,max(temp)])
##print(ans)
##

##ans=[ [i,max([j for j in range(1,11)if i%j==0])]
##      for i in range(100,110) ]
##print(ans)

ans=[]
for i in range(100,111):
    ans.append([i,max([j for j in range(1,11)if i%j==0])])
print(ans)
