str1 = input("Enter first word:")
str2 = input("Enter second word:")
if sorted(str1) == sorted(str2):
    print(f'{str1} and {str2} are anagrams')
else:
    print(f'{str1} and {str2} are not anagrams')