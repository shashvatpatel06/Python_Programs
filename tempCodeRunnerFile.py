str = input("Enter a string: ")
n = int(input("Enter no."))
l = str.split(" ")

if(n==1):
    for i in range(0,len(l)-n+1):
        print(l[i])   
elif(n==2):
    for i in range(0,len(l)-n+1):
        print(l[i],l[i+1])
elif(n==3):
    for i in range(0,len(l)-n+1):
        print(l[i],l[i+1],l[i+2])
else:
    print(str)
