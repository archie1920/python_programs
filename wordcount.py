import sys

# reading a multiple line input, ctr+d should be at the next line
print("enter multiple line, use ctr+d to end \n")
str1 = sys.stdin.read()
x = str1.split()
print(len(x))
print("number of words in the string are : ", len(x) )



