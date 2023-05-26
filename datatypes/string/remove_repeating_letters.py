# Remove the repeating letters from each word of a sentence
str1 = input("Type the sentence:")
str_low = str1.lower()
lst = str_low.split()
new_lst = []
for elem in lst:
    new_elem = ""
    for letter in elem:
        if letter not in new_elem:
            new_elem += letter
    new_lst.append(new_elem)
print(new_lst)
new_sentence = " ".join(new_lst)
print(new_sentence)
