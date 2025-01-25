# 1.)count no. of vowels in string

# str = input("Enter a string: ")
# count=0
# count = str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u')
# print("vowels in entered string is",count)

# 2.)convert all characters of string in lowe/upper/toggle case

# def tolower(str):
#     print("ToLower:",str.lower())
# def toupper(str):
#     print("ToUpper:",str.upper())
# def toggle(str):
#     print("Toggle:",str.swapcase())

# str = input("Enter a string: ")
# tolower(str),toupper(str),toggle(str)

# 3.)check whether one string is present in another or not

def check_string(str1,str2):
    if(str1==str2):
        return 3
        # print("Both strings are same")
    elif(str2 in str1):
        return 2
        # print("string 2 is present in string 1")
    elif(str1 in str2):
        return 1
        # print("string 1 is present in string 2")
    else:
        return 0
        # print("Both strings are different")
str1 = input("Enter String 1:")
str2 = input("Enter String 2:")
l1,l2 = len(str1),len(str2)

# 4.)if one string is present in another, Then remove that string

def remove_string(str1,str2):
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
remove_string(str1,str2)
