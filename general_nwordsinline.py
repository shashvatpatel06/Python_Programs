str = "Shashvat Patel is doing Python"
n = int(input("Enter no."))
l = str.split(" ")

i=0
while(i<len(l)):
    j=i
    while(j<n+i):
        if(n+i>len(l)):
            break
        print(l[j],end=" ")
        j+=1
    if(n+i>len(l)):
        break    
    print()
    i+=1