##nums=[11,22,33,44,55,66,77,88,99,]
##import math
##print(nums)
##
##result= list(map(math.sqrt,nums))
##print(result)


##nums=[11,22,33,44,55,66,77,88,99,]
##import math
##print(nums)
##
##result= [math.sqrt(i) for i in nums]
##print(result)


##nums=[11,22,33,44,55,66,77,88,99,]
##import math
##print(nums)
##
##result= [math.sqrt(i) for i in nums]
##print(result)

def add_five(x):
    temp=x+5
    return temp

nums=[11,22,33,44,55]
result=list(map(add_five,nums))
print(nums)
print(result)
print('-'*88)
