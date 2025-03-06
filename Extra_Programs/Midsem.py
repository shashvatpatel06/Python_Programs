'''a list contains rupee denominations like 500,200,100,50,20,10,5,2,1 
and accept amount from user and calculate minimum number of notes 
required for disbursement from Atm. 
If amount is 1254 the user will get 2 notes of 500,
1 note of 200, 1 note of 50,2 notes of 2 in python'''

l=[500,200,100,50,20,10,5,2,1]
d={}
n=int(input("Enter a number:"))
count=0
for i in l:
    t=n//i
    n=n-t*i
    d[i]=t
print("Dict:",d)
print("Usr will get:")
for i,j in d.items():
    if(j!=0):
        count+=j
        print(f"{j} notes of rupee {i}",end=", ")
print("Total minimum notes usr get:",count)



