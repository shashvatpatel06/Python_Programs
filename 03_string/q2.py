# 2.)convert all characters of string in lowe/upper/toggle case

def tolower(str):
    print("ToLower:",str.lower())
def toupper(str):
    print("ToUpper:",str.upper())
def toggle(str):
    print("Toggle:",str.swapcase())

str = input("Enter a string: ")
tolower(str),toupper(str),toggle(str)
