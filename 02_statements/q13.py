# 13.)Convert number 0 to 19 to its equivalent words. eg. 0->zero, 19->nineteen

def num_to_word(n):
    dict = {
    0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",
    9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
    16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"
    }
    return dict[n]
n = int(input("Enter the number: "))
print(n,"->",num_to_word(n))
