from math import sqrt,pow
# 1.)comparison between two numbers

# n1 = int(input("Enter number n1: "))
# n2 = int(input("Enter number n2: "))
# if(n1>n2):
#     print(f"n1 = {n1} is largest and n2 = {n2} is smallest")
# elif(n2>n1):
#     print(f"n2 = {n2} is largest and n1 = {n1} is smallest")
# else:
#     print("Both n1 and n2 are equal")

# 2.)comparison between three numbers

# n1 = int(input("Enter number n1: "))
# n2 = int(input("Enter number n2: "))
# n3 = int(input("Enter number n3: "))
# if(n1>=n2 and n1>=n3):
#     if(n1==n2==n3):
#         print("All three are equal")
#     elif(n1==n2):
#         print("n1 = n2 and it is largest")
#     elif(n1==n3):
#         print("n1 = n3 and it is largest")  
#     elif(n1>n2 and n1>n3):
#         print("n1 is largest")  
# elif(n2>=n1 and n2>=n3):
#     if(n1==n2==n3):
#         print("All three are equal")
#     elif(n2==n1):
#         print("n1 = n2 and it is largest")
#     elif(n2==n3):
#         print("n2 = n3 and it is largest")  
#     elif(n2>n1 and n2>n3):
#         print("n2 is largest")
# elif(n3>=n1 and n3>=n2):
#     if(n1==n2==n3):
#         print("All three are equal")
#     elif(n3==n1):
#         print("n3 = n1 and it is largest")
#     elif(n3==n2):
#         print("n3 = n2 and it is largest")
#     elif(n3>n1 and n3>n2):
#         print("n3 is largest")

# 3.)no. is even or not

# n = int(input("Enter a number:"))
# if(n%2==0):
#     print("number is even")
# else:
#     print("number is odd")

# 4.)no. is divisible by 10 or not

# n = int(input("Enter a number:"))
# if(n%10 == 0):
#     print("number is divisible by 10")
# else:
#     print("number is not divisible by 10")

# 5.)major/Minor

# age = int(input("Enter your age: "))
# if(age<18):
#     print("Minor")
# else:
#     print("Major")

# 6.)length of number

# n = input("Enter a number: ")
# print(len(n))

# 8.)Check whether a triangle is Valid or not

# a1 = float(input("Enter angle 1: "))
# a2 = float(input("Enter angle 2: "))
# a3 = float(input("Enter angle 3: "))
# if(a1+a2+a3 == 180):
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")

# 9.)Print Absolute value of number

# n = float(input("Enter number: "))
# if(n>=0):
#     print("Absolute number:",n)
# else:
#     print("Absolute number:",abs(n))

# 10.)Comparison between Area, Perimeter of Rectangle

# l,b = 3,3.4
# p= 2*l+2*b
# a = l*b
# if(p>a):
#     print("perimeter > Area")
# elif(a>b):
#     print("Area > Perimeter")
# else:
#     print("Area = Perimeter")

# 11.)Check whether three points lies on same line or not

# x1,y1 = map(float,input("Enter coordinates x1,y1:").split(","))
# x2,y2 = map(float,input("Enter coordinates x2,y2:").split(","))
# x3,y3 = map(float,input("Enter coordinates x3,y3:").split(","))
# condition = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
# if(condition == 0):
#     print("Three points are collinear")
# else:
#     print("Three points are not collinear")

# 12.)Find location of point wrt. circle

# a,b = map(float,input("Enter coordinates of circle: ").split(","))
# r =float(input("Enter radius: "))
# x,y = map(float,input("Enter the coordinates of point: ").split(","))
# k = sqrt(pow(x-a,2)+pow(y-b,2))
# if(k>r):
#     print("point lies outside the circle")
# elif(k<r):
#     print("point lies inside the circle")
# else:
#     print("point lies on the circle")   

# 13.)Convert number 0 to 19 to its equivalent words. eg. 0->zero, 19->nineteen

# def num_to_word(n):
#     dict = {
#     0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",
#     9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
#     16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"
#     }
#     return dict[n]
# n = int(input("Enter the number: "))
# print(n,"->",num_to_word(n))

# 14.)print grade according to marks 

# def grade(m):
#     if(80<=m<=100):
#         return "grade:O"
#     elif(70<=m<=79):
#         print("grade:A+")
#     elif(60<=m<=69):
#         return "grade:A"
#     elif(55<=m<=59):
#         return "grade:B+" 
#     elif(50<=m<=54):
#         return "grade:B"
#     elif(45<=m<=49):
#         return "grade:C"
#     elif(40<=m<=44):
#         return "grade:P"  
#     elif(0<=m<=39):
#         return "Fail, grade:F"
#     else:
#        return "NA"
# s1 = float(input("Enter marks of Subject 1: "))
# s2 = float(input("Enter marks of Subject 2: "))
# s3 = float(input("Enter marks of Subject 3: "))
# total = s1+s2+s3
# avg = total/3
# print("Total =",total,"Average =",avg)
# print("grade in Subject 1:",grade(s1))
# print("grade in Subject 2:",grade(s2))
# print("grade in Subject 3:",grade(s3))



