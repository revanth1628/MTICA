class Rectangle:
    def __init__(self,length,breadth):
        assert(length>=0 and breadth>=0),'INVALID'
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    def peri(self):
        return 2*(self.length+self.breadth)

r=int(input('enter the length :'))
t=int(input('enter the breadth :'))
try:
    
    s=Rectangle(r,t)
    print(s.area())
    print(s.peri())
except AssertionError as rev:
    print(rev)
