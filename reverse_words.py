def reverse_words(my_sent):
      # split the sentence in to the list
      new_list = my_sent.split(" ")
      #print(new_list)
      # reverse each words from the list
      rev_list = [each_word[::-1] for each_word in new_list]
      return rev_list



given_str = "This is my test"
# print the list as a sentence
print(" ".join(reverse_words(given_str)))
