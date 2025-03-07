# 2.)comparison between three numbers

n1 = float(input("Enter number n1: "))
n2 = float(input("Enter number n2: "))
n3 = float(input("Enter number n3: "))
if(n1==n2==n3):
        print("All three are equal")
elif(n1>=n2 and n1>=n3):
    if(n1==n2):
        print("n1 = n2 and it is largest")
    elif(n1==n3):
        print("n1 = n3 and it is largest")  
    elif(n1>n2 and n1>n3):
        print("n1 is largest")  
elif(n2>=n1 and n2>=n3):
    if(n2==n1):
        print("n1 = n2 and it is largest")
    elif(n2==n3):
        print("n2 = n3 and it is largest")  
    elif(n2>n1 and n2>n3):
        print("n2 is largest")
elif(n3>=n1 and n3>=n2):
    if(n3==n1):
        print("n3 = n1 and it is largest")
    elif(n3==n2):
        print("n3 = n2 and it is largest")
    elif(n3>n1 and n3>n2):
        print("n3 is largest")
