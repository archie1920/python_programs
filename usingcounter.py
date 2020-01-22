from collections import Counter

c=Counter(['a','b','c','a','b','a'])
print(c)

#use file --> C:\TestNew\SampleText.txt
filename = input("Enter file path :")
f = open(filename, 'r')
words = []
for line in f:
    words += line.split()
f.close()

X = Counter(words)
print(X)
print("\nTop words are \n", X.most_common(5))



