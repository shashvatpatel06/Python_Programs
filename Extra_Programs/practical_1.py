def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
s = "Welcome"
p=[]
i=5
while(len(p)<=len(s)):
    if(isPrime(i)):
        p.append(i)
    i+=1    
s1=''
for i in range(0,len(s)):
    s1+=chr(ord(s[i])+(pow(-1,i)*p[i]))
print(s1)
'''
print(chr(ord('W')+5))
print(chr(ord('e')-7))
print(chr(ord('l')+11))
print(chr(ord('c')-13))
print(chr(ord('o')+17))
print(chr(ord('m')-19))
print(chr(ord('e')+23))
'''




