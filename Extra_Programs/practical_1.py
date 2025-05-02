def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
s = "Welcome"
p=[]
for i in range(5,100):
    if(prime(i)):
        p.append(i)
print(p)
l=[]
for i in range(0,len(s)):
    l.append(chr(ord(s[i])+(pow(-1,i)*p[i])))
    
print     
s1=''
for i in range(0,len(l)):
    s1+=l[i]
print(s1)
'''
print(chr(ord('W')+5))
print(chr(ord('e')-7))
print(chr(ord('l')+11))
print(chr(ord('c')-13))
print(chr(ord('o')+17))
print(chr(ord('m')-19))
print(chr(ord('e')+23))

def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
s = "Welcome"
p=[]
for i in range(5,100):
    if(prime(i)):
        p.append(i)
print(p)
l=[]
    
t=p[0]
m=1
for i in range(0,len(s)):
    for j in range(t,100):
        if(m==1):
            if(prime(j)):
                l.append(chr(ord(s[i])+j))
                m=2
                t=p[i+1]
                break
        if(m==2):
            if(prime(j)):
                l.append(chr(ord(s[i])-j))
                m=1
                t=p[i+1]
                break
s1=''
for i in range(0,len(l)):
    s1+=l[i]
print(s1)
'''


