# 11.)Check whether three points lies on same line or not

x1,y1 = map(float,input("Enter coordinates x1,y1:").split(","))
x2,y2 = map(float,input("Enter coordinates x2,y2:").split(","))
x3,y3 = map(float,input("Enter coordinates x3,y3:").split(","))
condition = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
if(condition == 0):
    print("Three points are collinear")
else:
    print("Three points are not collinear")
