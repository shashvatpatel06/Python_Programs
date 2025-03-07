# 4.)check whether a number is prime, palindrome, perfect, armstrong

n = int(input("Enter a number:"))
def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count>0):
        print(n,"is not a prime no.")
    else:
        print(n,"is a prime no.")
def palindrome(n):
    num,t = n,0
    while(n>0):
        r=n%10
        t = t*10+r
        n=int(n/10)
    if(t==num):
        print(num,"is palindrome")
    else:
        print(num,"is not palindrome")
def perfect(n):
    total=0
    for i in range(1,n):
        if(n%i==0):
            total += i
    if(n==total):
        print(n,"is a perfect no.")
    else:
        print(n,"is not a perfect no.")
def armstrong(n):
    temp,l=n,0
    while(temp>0):
        l +=1
        temp = int(temp/10)
    total,num=0,n
    while(n>0):
        total += pow(n%10,l)
        n = int(n/10)
    if(total==num):
        print(num,"is an armstrong no.")
    else:
        print(num,"is not an armstrong no.")
prime(n)
palindrome(n)
perfect(n)
armstrong(n)

