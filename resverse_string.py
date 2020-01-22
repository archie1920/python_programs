#python program without built-in function to reverse the string

#text = "abcd"
text = input("Enter the string : ")
if text == "":
    print("Please enter a valid string!")
    text = input("Enter the string : ")

str1 =""
for i in range(len(text)-1, -1, -1):
    #print(text[i],end="")
    str1 = str1+text[i]

print("Reverse of the string you entered is : ",str1)