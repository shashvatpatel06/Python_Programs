# 12.)Find location of point wrt. circle

from math import sqrt  
a,b = map(float,input("Enter coordinates of circle i.e.(x,y): ").split(","))
r =float(input("Enter radius: "))
x,y = map(float,input("Enter the coordinates of point i.e.(x,y): ").split(","))
k = sqrt(pow(x-a,2)+pow(y-b,2))
if(k>r):
    print("point lies outside the circle")
elif(k<r):
    print("point lies inside the circle")
else:
    print("point lies on the circle")   
