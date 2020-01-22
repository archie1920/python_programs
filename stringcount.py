
# Python Program to Count Vowels and Consonants in a String
def str_check1(str1):
#str1 = input("Please Enter Your Own String : ")
    vowels = 0
    consonants = 0
    str1.lower()

    for i in str1:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1

    print("Total Number of Vowels in this String = ", vowels)
    print("Total Number of Consonants in this String = ", consonants)

def str_check_array(str1):
 #print("Method 2")
    vowel = ['a', 'e', 'i', 'o', 'u']
#Sentence = input("Enter a phrase: ")
    countv = 0
    countc = 0
    for letter in str1:
        if letter in vowel:
            countv += 1
        else:
            countc += 1
    print("vowels count is:", countv)
    print("consonants count is:", countc)

def str_check_uplw(str1):
    #print("Method 3 check for both lower case and upper case")
    strvowel = "aeiouAEIOU"
    countv1 = 0
    countc1 = 0
    for i in str1:
         if i in strvowel:
             countv1 += 1
         else:
            countc1 += 1
    print("vowels count is:", countv1)
    print("consonants count is:", countc1)

def main():
    input_str = input("Please Enter Your Own String : ")
    print("Method 1 : Vowel check both upper case and lower case using string")
    str_check_uplw(input_str)
    print("Method 2 : Vowel check using in if condition")
    str_check1(input_str)
    print("Method 3 : Vowel check using array ")
    str_check_array(input_str)


if __name__ == '__main__' :
    main()
