#Palindrome number

rev = 0
def int_reverse(n):
    global rev
    if n > 0 :
     rmd = n % 10
     rev = (rev * 10) + rmd
     int_reverse( n // 10)
    return rev


num = int(input("Enter a number you want to check : "))
new_num = int_reverse(num)
print("reverse number is : ", new_num)

if num == new_num:
    print("So",num, "is Palindrome number. ")
else :
    print(num,"is not a Palindrome number")


#n=int(input("Enter number:"))
temp=num
rev=0
while num > 0:
    dig = num % 10
    rev = rev*10 + dig
    num = num // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
