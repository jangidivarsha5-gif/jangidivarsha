class cricle:
   def __init__(self):
       x=int(input("Enter radius: "))
       self.r=x
   def display(self):
       print("Area is ",3.14*self.r**2)
       
a=int(input("Enter num of circle: "))
l=[]
for i in range(a):
    c=cricle()
    l.append(c)
    c.display()
    print("_________")
