# 8.)factorial
def fact(n):
   if(num>0):
        i=num-1
        while(i>0):
            num = num*i
            i -= 1
        return num
    else:
        return 1
n = int(input("Enter a number:))
print("factorial of",n,"is",fact(n))
