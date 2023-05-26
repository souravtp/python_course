"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"r+" - read and write permission.

In addition, you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""


# file1 = open("samplefile.txt", "w")  # putting "x" only creates file. It won't have any content.
# # If we put "w", we have to write the content also.
# file1.write("Hello, world!")
# file1.close()

# file1 = open("samplefile.txt", "a")
# file1.write(" welcome to the python course.")
# file1.write("\nThis is a file for testing file handling.")
# file1.write("\nthis would be printed in the same line if newline character (\\n) was not used.")
# file1.close()

# f = open("samplefile.txt", "w")  # If we open the file again with "w", and write anything,
# all the contents will be rewritten.
# f.write("hii")
# f.close()

# file1 = open("samplefile.txt", 'r')
# print(file1.read())
# file1.close()

# file1 = open("samplefile.txt", "r")
# print(file1.read(5))
# print(file1.readline())  # here the 'Hello' part is removed.
# # If we use readline() once, the first line will get printed.
# # If we use it again we can print first two lines and so on.
# file1.close()

# file1 = open("samplefile.txt", "r")
# print(file1.readline())
# print(file1.readlines())  # Here the lines will be added as elements of a list.

# with open("samplefile.txt", "r") as f:
#     lines = f.readlines()
#     lines1 = [line.rstrip() for line in lines]
#     print(lines1)
#     # for line in lines:
#     #     print(line.rstrip())
# f.close()

"""truncate() function"""

# with open(r'C:\Users\soura\Desktop\file_handling_test\truncate_test.txt', 'w') as f:
#     f.write("apple\nbanana\ncat\ndoll\nelephant")
# f.close()
#
# with open(r'C:\Users\soura\Desktop\file_handling_test\truncate_test.txt', 'r+') as t:
#     t.truncate(15)  # the argument is the byte value.
#     print(t.read())

"""to search a word in entire directory"""
import os


def search_files(start_dir, keyword):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, encoding='utf-8') as f:
                    for line in f:
                        if keyword in line:
                            print(f"{keyword} found in {file_path}")


search_files('C:/Users/soura/PycharmProjects/pythoncourse', 'find(')
