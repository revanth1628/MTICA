##i=input()
##temp=i.split()
##i=0
##while(i<len(temp)):
##    print(len(temp[i]),end=' ')
##    i=i+1




def solveproblem(s):
    lst=s.split()
    return [len(i) for i in lst]
i=input()
print(solveproblem(i))

    
