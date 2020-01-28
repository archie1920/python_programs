def isomorphic(str1, str2):
    temp_dict = {}
    #print(str1, str2)
#check if both the strings are same
    if str1 == str2:
        print("Both the string are same")
        return True
#check if length of both the string is same or not
    if len(str1) != len(str2):
        print("Length mismatch")
        return False
#save the str1 in the dictionary with value NONE
    for i in str1:
        temp_dict[i] = None
#now check if the key-value pair of the dictionary
    x = 0
    for i in str1:
        #print(temp_dict)
        if temp_dict[i] is None:
            temp_dict[i] = str2[x]
            x += 1
        elif temp_dict[i] == str2[x]:
            x += 1
        else:
            return False
    return True


def main():
    value1 = input("Enter 1st string: ")
    value2 = input("Enter 2nd string: ")

    val = bool(isomorphic(value1, value2))
    #print("val:", val)
    if val:
        print("Given strings are isomorphic")
    else:
        print("Given strings are not isomorphic")


if __name__ == '__main__':
    main()

