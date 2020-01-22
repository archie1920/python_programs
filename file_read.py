
def wordcount(fname):
    num_words = 0
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
            #print(len(words))
    print("Number of words:", num_words, "\n")
    #print(num_words)
    f.close()

def file_print(fname):
    #print the content of the file
    file1 = open(fname,'r')
    for line in file1:
        print(line)
    file1.close()

def main():
    filename = input("Enter the file path: ")
    # for testing use file --> C:\Users\Archana Yeole\Desktop\neil.txt
    wordcount(filename)
    file_print(filename)

if __name__ == '__main__':
    main()
