from math import pow
# 1.)print all alphabets in upper and lower case

# for i in range(65,91):
#     print(chr(i),end=" ")
# print()
# for i in range(97,123):
#     print(chr(i),end=" ")

# 2.)print multiplication table for a number

# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# 3.)count no. of alphabets and digits in given string

# str = input("Enter a string: ")
# digits,alphabets = 0,0
# for i in str:
#     if(i.isalpha()):
#         alphabets+=1
#     elif(i.isdigit()):
#         digits+=1   
# print("In String",str,"no. of digits are",digits,"and no. of alphabets are",alphabets)

# 4.)check whether a number is prime, palindrome, perfect, armstrong

# n = int(input("Enter a number:"))
# def prime(n):
#     count=0
#     for i in range(2,n):
#         if(n%i==0):
#             count+=1
#     if(count>0):
#         print(n,"is not a prime no.")
#     else:
#         print(n,"is a prime no.")
# def palindrome(n):
#     num,t = n,0
#     while(n>0):
#         r=n%10
#         t = t*10+r
#         n=int(n/10)
#     if(t==num):
#         print(num,"is palindrome")
#     else:
#         print(num,"is not palindrome")
# def perfect(n):
#     total=0
#     for i in range(1,n):
#         if(n%i==0):
#             total += i
#     if(n==total):
#         print(n,"is a perfect no.")
#     else:
#         print(n,"is not a perfect no.")
# def armstrong(n):
#     temp,l=n,0
#     while(temp>0):
#         l +=1
#         temp = int(temp/10)
#     total,num=0,n
#     while(n>0):
#         total += pow(n%10,l)
#         n = int(n/10)
#     if(total==num):
#         print(num,"is an armstrong no.")
#     else:
#         print(num,"is not an armstrong no.")
# prime(n)
# palindrome(n)
# perfect(n)
# armstrong(n)

# 6.)print the hours with am/pm

# h = int(input("Enter hours:"))
# dict = {
#     13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,
#     21:9,22:10,23:11,24:12}
# if(0<h<12):
#     print(h,"am")
# elif(12<=h<24):
#     print(dict[h],"pm")

# 7,8.)nCr and nPr

#     if(num>0):
#         i=num-1
#         while(i>0):
#             num = num*i
#             i -= 1
#         return num
#     else:
#         return 1
# n = int(input("Enter n:"))
# r = int(input("Enter r:"))
# if(n>r):
#     print("nCr =",fact(n)/(fact(n-r) * fact(r)))
#     print("nPr =",fact(n)/fact(n-r))
# else:
#     print("nCr =",1)
#     print("nPr =",fact(n))

# 9.)print n natural no. in reverse
# n = int(input("Enter number:"))
# i=n
# while(i>0):
#     print(i)
#     i -= 1





