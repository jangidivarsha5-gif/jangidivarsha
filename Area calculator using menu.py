def sq():
    s=int(input("Enter side: "))
    print("Area: ",s*s)
def rect(a,b):
    print("AREA: ",a*b)
def cir():
    r=int(input("Enter radius: "))
    return 3.14*r*r
def tri(b,h):
    return 0.5*b*h


while True:    
    print("Area Calcuator")
    print("1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n5. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        sq()
    elif ch==2:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        rect(l,b)
    elif ch==3:
        x=cir()
        print("AREA: ",x)
    elif ch==4:
        b=int(input("Enter base: "))
        h=int(input("Enter height: "))
        y=tri(b,h)
    else:
        break
