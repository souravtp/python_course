# import os.path
#
# file_path = r'C:\Users\soura\PycharmProjects\pythoncourse\file_handling\samplefile.txt'
#
# flag = os.path.exists(file_path)
#
# if flag:
#     print(f'The file {file_path} exists.')
# else:
#     print(f'the file {file_path} does not exist.')
#

"""to get the file size"""
# file_size = os.path.getsize(file_path)
# print(f'size of {file_path} is {file_size} bytes.')

"""To delete lines from a file """
# path = r"C:/users/soura/Desktop/file_handling_test/test_file.txt"
# with open(r"C:/users/soura/Desktop/file_handling_test/test_file.txt") as fr:
#     lines = fr.readlines()  # newlines are separated based on where we pressed 'enter' while typing the document.
#     ptr = 1
#     with open(path, "w") as fw:
#         for line in lines:
#             if ptr != 5:
#                 fw.write(line)
#             ptr += 1
#         print("deleted")

"""another method"""

"""creating file with names of months for testing"""
# with open(r"C:/users/soura/Desktop/file_handling_test/months.txt", "w") as mn:
#     mn.write(
#         "1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n"
#         "10. October\n11. November\n12. December")
# mn.close()

# with open(r"C:/users/soura/Desktop/file_handling_test/months.txt", "r+") as mn:
#     lines = mn.readlines()
#     mn.seek(0)  # this will move the file pointer to the beginning of the file.
#     mn.truncate(0)  # this function truncates(empties) the txt file.
#     mn.writelines(lines[1:])  # this will enter the list elements back to the txt file from second element of list.

# """seek() function"""
# with open()


"""to create a pyramid pattern"""
# height = 5
# with open(r'C:/users/soura/Desktop/file_handling_test/pattern.txt', 'w') as fp:
#     for i in range(height):
#         spaces = "  "*(height-i-1)
#         stars = " * " * (i+1)
#         fp.write(spaces+stars+'\n')


"""to copy elements from one file to another"""
# with open(r"C:/users/soura/Desktop/file_handling_test/months.txt", "r+") as fo:
#     fc = open(r"C:/users/soura/Desktop/file_handling_test/months_copy.txt", "w")
#
#     for i in fo:
#         fc.write(i)

"""search for a string in text file"""
x = input("enter the world to search:")
with open(r"C:/users/soura/Desktop/file_handling_test/months.txt", "r") as mn:
    for i in mn:
        if i.find(x) != -1:
            print(f'the word {x} exists in the file')
            break
    else:
        print("not present")
