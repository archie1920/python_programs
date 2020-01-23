#program to revers the given string

def revstr(s):
    if len(s) == 0:
        return s
    else:
        return revstr(s[1:]) + s[0]


str1 = input("Please enter the string : ")

print("You entered '",str1,"'")

str2 = revstr(str1)

print("Reverse string is :",str2)

if str1 == str2:
    print("string is palindrome")
else:
    print("String is not palindrome")