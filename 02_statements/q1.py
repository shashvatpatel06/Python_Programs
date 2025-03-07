# 1.)comparison between two numbers

n2 = float(input("Enter number n2: "))
n1 = float(input("Enter number n1: "))
if(n1>n2):
    print(f"n1 = {n1} is larger and n2 = {n2} is smaller")
elif(n2>n1):
    print(f"n2 = {n2} is larger and n1 = {n1} is smaller")
else:
    print("Both n1 and n2 are equal")
