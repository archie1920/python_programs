text = "hello this is hello this is baby baby baby baby hello"

word_list = text.split()

#create empty dictionary

word_count = dict()

for x in word_list:
    if x in word_count:
        word_count[x] = word_count[x] + 1
    else:
         word_count[x] = 1


for word in list(word_count.keys()):
  print(word, ":" ,word_count[word])



