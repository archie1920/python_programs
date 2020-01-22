text1 = input("enter a string: ")
text2 = input("enter 2 nd string to test anagram : ")

if len(text1) == len(text2):
    """sorted(text1)
    sorted(text2)
    print(text1," ", text2)"""
    if sorted(text1) == sorted(text2):
       print("Given words are anagram")
    else:
       print("Given words are not anagram")
else:
    print("Given words are not anagram - length mismatch")


