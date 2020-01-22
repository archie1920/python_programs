#reverser the entered array



num = [1,2,3,4,5]
print("array values are : ",num)
i = 0
j = len(num)-1
temp  = 0
while i < j :
    temp = num[i]
    num [i] = num [j]
    num [j] = temp
    #print(num)
    i += 1
    j -= 1

print("reverse is : ", num)