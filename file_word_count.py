#2 functions to return the word count from the file and top 10 most repeated words from the file
from collections import Counter

def openfile(filename):
    file_h = open(filename, 'r')
    return file_h

def total_word(fh):
    word_list = []
   # with open(filename,'r') as f1:
    for line in fh:
        word_list += line.split()
    #f1.close()
    return(word_list)

def top_10words(wlist, nc):
    X = Counter(wlist)
    r =int(nc)
    print(X.most_common(r))

def main():
    fname = input("Enter the file path :  ")
    # for testing use file --> C:\Users\Archana Yeole\Desktop\neil.txt or C:\TestNew\SampleText.txt
    if len(fname) == 0:
        print("Enter valid file name and path!")
    else:
        my_file = openfile(fname)
        word_list = total_word(my_file)
        print("The Total word count is: ",len(word_list))
        num = input("Enter the number of high frequency words you want to see : ")
        print("The top ",num," high frequency words are :")
        top_10words(word_list, num)
        my_file.close()

if __name__ == '__main__':
    main()


