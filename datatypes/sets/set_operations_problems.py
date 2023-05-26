# count vowels
# x = input("enter the sentence:")
# S1 = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
# counter = 0
# for i in x:
#     if i in S1:
#         counter +=1
# print(f'The number of vowels in the sentence is{counter}')

# common elements
# x = input("Enter first string:")
# S1 = set(x.lower())
# y = input("Enter second string:")
# S2 = set(y.lower())
# S3 = S1.intersection(S2)
# print(f'common letters in the entered strings:{S3}')

# letters in first string not in second
# x = input("Enter first string:")
# S1 = set(x.lower())
# y = input("Enter second string:")
# S2 = set(y.lower())
# S3 = S1.difference(S2)
# print(f'letter in first string and not in second are:{S3}')

# letters in both lists
# x = input("Enter first string:")
# S1 = set(x.lower())
# y = input("Enter second string:")
# S2 = set(y.lower())
# S3 = S1.union(S2)
# print(f'letters in both strings are:{S3}')

# letters are in two strings but not in both
# x = input("Enter first string:")
# S1 = set(x.lower())
# y = input("Enter second string:")
# S2 = set(y.lower())
# S3 = S1.symmetric_difference(S2)
# print(f'letters in two strings but not in both are:{S3}')

# intersection of sets
# S1 = {"apple", "orange", "pineapple", "tomato", "coconut"}
# S2 = {"ginger", "coconut", "chilli", "onion", "tomato"}
# S3 = S1.intersection(S2)
# print(f'intersection of S1 and S2:{S3}')

# Union of sets
# S1 = {"apple", "orange", "pineapple", "tomato", "coconut"}
# S2 = {"ginger", "coconut", "chilli", "onion", "tomato"}
# S3 = S1.union(S2)
# print(f'union of S1 and S2: {S3}')

# Set difference
# S1 = {"apple", "orange", "pineapple", "tomato", "coconut"}
# S2 = {"ginger", "coconut", "chilli", "onion", "tomato"}
# S3 = S1.difference(S2)
# print(f'set difference: {S3}')

# Symmetric difference
# S1 = {"apple", "orange", "pineapple", "tomato", "coconut"}
# S2 = {"ginger", "coconut", "chilli", "onion", "tomato"}
# S3 = S1.symmetric_difference(S2)
# print(f'symmetric difference: {S3}')

# Check whether subset or not
# S1 = {"a", "b", "c", "d", "e", "f"}
# S2 = {"b", "c", "e", "z"}
# if S2.issubset(S1):
#     print(f'{S2} is a subset of {S1}')
# else:
#     print(f'{S2} is not a subset of {S1}')