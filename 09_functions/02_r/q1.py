def primeFactors(n,l=[],i=2):
    if(n<=1):
        return l
    elif(n%i==0):
        l.append(i)
        return primeFactors(n//i,l,i)
    else:
        return primeFactors(n,l,i+1)

n = int(input("Enter a number:"))
print(primeFactors(n))
