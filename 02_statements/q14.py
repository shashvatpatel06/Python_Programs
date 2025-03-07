# 14.)print grade according to marks 

def grade(m):
    if(80<=m<=100):
        return "grade:O"
    elif(70<=m<=79):
        print("grade:A+")
    elif(60<=m<=69):
        return "grade:A"
    elif(55<=m<=59):
        return "grade:B+" 
    elif(50<=m<=54):
        return "grade:B"
    elif(45<=m<=49):
        return "grade:C"
    elif(40<=m<=44):
        return "grade:P"  
    elif(0<=m<=39):
        return "Fail, grade:F"
    else:
       return "NA"
s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
total = s1+s2+s3
avg = total/3
print("Total =",total,"Average =",avg)
print("grade in Subject 1:",grade(s1))
print("grade in Subject 2:",grade(s2))
print("grade in Subject 3:",grade(s3))

