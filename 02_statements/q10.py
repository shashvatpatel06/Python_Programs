# 10.)Comparison between Area, Perimeter of Rectangle

l = float(input("Enter length of rectangle:"))
b = float(input("Enter breadth of rectangle"))
p = 2*(l+b)
a = l*b
if(p>a):
    print("perimeter > Area")
elif(a>b):
    print("Area > Perimeter")
else:
    print("Area = Perimeter")
