# 6.)length of number

n = str(input("Enter a number: "))
if("." in n):
    print("Length",len(n)-1)
else:
    print("Length",len(n))
