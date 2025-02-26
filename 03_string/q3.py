# 3.)check whether one string is present in another or not

def check_string(str1,str2):
    if(str1==str2):
        print("Both strings are same")
        return 1
    elif(str2 in str1):
        print("string 2 is present in string 1")
        return 2
    elif(str1 in str2):
        print("string 1 is present in string 2")
        return 1
    else:
        print("Both strings are different")
        return 0
str1 = input("Enter String 1:")
str2 = input("Enter String 2:")
check_string(str1,str2)