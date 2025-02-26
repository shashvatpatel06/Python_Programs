# 4.)if one string is present in another, Then remove that string

def check_string(str1,str2):
    if(str1==str2):
        return 1
    elif(str2 in str1):
        return 2
    elif(str1 in str2):
        return 1
    else:
        return 0

def remove_string(str1,str2):
    l1,l2 = len(str1),len(str2)
    r = check_string(str1,str2)
    if(r==1):
        a = str2.index(str1)
        string2 = str2[0:a]+str2[a+l1:l2+1]
        print(string2)
    elif(r==2):
        a = str1.index(str2)
        string1 = str1[0:a]+str1[a+l2:l1+1]
        print(string1)
    elif(r==3):
        print("Empty string")
    else:
        print("Both string are different")

str1 = input("Enter String 1:")
str2 = input("Enter String 2:")
check_string(str1,str2)
remove_string(str1,str2)