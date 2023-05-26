# str1 = "james"
# n = len(str1)//2
# print(str1[::n])

# s1 = "hello"
# s2 = "world"
# l = len(s1)
# mid = int(l/2)
# first = s1[:mid]
# last = s1[mid:]
# x = first+s2+last
# print(x)


# to print lower and upper case
# str1 = "HelLo WorLd"
# l = len(str1)
# i = 0
# lower = ""
# upper = ""
# special = ""
# while i < l:
#     if str1[i].islower():
#         lower += str1[i]
#     elif str1[i].isupper():
#         upper += str1[i]
#     else:
#         special += str1[i]
#     i += 1
# str2 = lower+upper
# print(str2)

# To count letters, digits and special symbols in the given string

# str1 = "s2|35$l#4hh*+&D($^"
# alpha = 0
# digit = 0
# special_chr = 0
# for i in str1:
#     if i.isalpha():
#         alpha += 1
#     elif i.isnumeric():
#         digit += 1
#     else:
#         special_chr += 1
# print(f'alphabets={alpha}, digit={digit}, special characters={special_chr}')


"""to create my own split function"""


def split_string(input_str):
    # Create an empty list to store the words
    words = []

    # Create a variable to keep track of the start of each word
    start = 0
    if input_str.isspace() or input_str == "":
        return []

    else:
        # Loop over each character in the string
        for i in range(len(input_str)):
            # Check if the character is a space
            if input_str[i] == " ":
                # If it is, add the word to the list
                if not input_str[start:i].isspace():
                    words.append(input_str[start:i])
                # Update the start variable to the next word
                start = i + 1

    # Add the last word to the list
    words.append(input_str[start:])

    return words


print(split_string("To be or not to be, that is the question"))
print(split_string("To be or not to be,that is the question"))
print(split_string("   "))
print(split_string(" abc "))
print(split_string(""))
