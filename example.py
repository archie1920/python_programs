#arr = {10, 20, 30, 40, 50}
revstr = input("enter the array : ")
revstr_list = revstr.split(' ')
fnum = 0
lnum = len(revstr_list)-1
temp = ""

while fnum < lnum :
#    print(revstr_list[fnum],end="")
    temp = revstr_list[lnum]
    revstr_list[lnum] = revstr_list[fnum]
    revstr_list[fnum] = temp
    #print(revstr_list[fnum],end=" ")
    fnum += 1
    lnum -= 1

print("\nreverse list is : ", revstr_list)


#\------------------------------
str1 = ["abc", "xyz", "tre", "puy", "xyz", "tre"]
print(str1)
#j = 0
str2 =[]
for i in range(0, len(str1)):
   for x in range(i + 1, len(str1)):
      if str1[i] == str1[x]:
         str2.append(str1[i])
         x += 1
         #j += 1
      else:
         x += 1
   i += 1
print(str2)