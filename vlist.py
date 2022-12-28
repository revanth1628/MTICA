
dict1={"dev":1500,"teva":2000,"ysuri":2500,"prasad":1600,"jeev":2400,"jothsna":13600,"chandu":7,"tej":100}
ans=[]
for i in dict1:
    if dict1[i]<5000:
        ans.append(i.upper())
print(ans)


dict1={"dev":1500,"teva":2000,"ysuri":2500,"prasad":1600,"jeev":2400,"jothsna":13600,"chandu":7,"tej":100}
ans=[i.upper() for i in dict1 if dict1[i]<5000]
print(ans)



lst=["rev","dev","","","suri",' ','']
ans=[]
for i in lst:
    if i:
        ans.append(i)
print(ans)


lst=["rev","dev","","","suri",' ','']
ans=[i for i in lst if i]
print(ans)



for i in range(5):
    inp=input()
    if inp:
        print("hello "+inp)
    else:
        print("tata "+inp)





