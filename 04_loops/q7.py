# 7.)nCr and nPr
def fact(n):
   if(num>0):
        i=num-1
        while(i>0):
            num = num*i
            i -= 1
        return num
    else:
        return 1
n = int(input("Enter n:"))
r = int(input("Enter r:"))
if(n>r):
    print("nCr =",fact(n)/(fact(n-r) * fact(r)))
    print("nPr =",fact(n)/fact(n-r))
else:
    print("nCr =",1)
    print("nPr =",fact(n))
