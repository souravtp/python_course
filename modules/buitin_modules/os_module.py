import os

print(dir(os))


"""
to create a directory"""
# os.mkdir(r"C:\Users\soura\PycharmProjects\pythoncourse\modules\folder_created_with_os_module")
"""
we can give a path or folder name2 as argument. if we give a path directory will created in that path.
if we enter the folder name2 it will be created in the current working directory.
"""


""" 
to get current working directory.  The current working directory is the folder in which
the Python script is operating.
"""
# print(os.getcwd())


""" chdir() is used to change the directory"""
# print(os.chdir("../"))


# def current_path():
#     print("current working directory:")
#     print(os.getcwd())
#     print()


# current_path()  # by default cwd is the directory where the code is located
#
# os.chdir('../')  # this will change the cwd to the parent directory. this file will not be moved. After this we can
# make changes or perform operations in new working directory.
#
# current_path()  # this will output the parent directory of the default directory.
#
# print(os.name2)  # this will give output 'nt' for windows. 'posix' for unix like os, mac and linux.


# os.mkdir('D:/sampledir')
# os.rmdir('D:/sampledir')  # to delete the directory.

"""
os.path.join() is used to join one or more path components intelligently to return a complete path string.
It does not create a directory, but returns a joined string. we can give this string to mkdir() to create 
a directory.
"""
# parent_dir = "C:/users/soura/documents"
# new_dir = "created_using_join()_and_mkdir()"
# full_path = os.path.join(parent_dir, new_dir)
# if not os.path.exists(full_path):
#     os.mkdir(full_path)
# else:
#     print("directory already exists:", full_path)

"""
os.makedirs() -- this function can create a parent directory and child directory at once. 
It is different from mkdir(). mkdir() can create one directory at once. we have to repeat the function
to create inner directories. but in makedirs() can create all at once, if parent directory does not 
exist, it will create it without any error. It accepts one more argument named mode. By default mode
value is 0o777(represents octal) which grants read, write, and execute permissions to the owner, group, and other users.
You can modify this value to suit your needs.
for read and write permissions for the owner and read permissions for the group and other users we use mode = 0o644
"""
# try:
#     os.makedirs('C:\\Users\\soura\\Desktop\\os_function_test', mode=0o777)
# except FileExistsError:
#     print("file already exists")

"""listdir() lists all files and directories in the specified directory"""
print(os.listdir('C:/users/soura/PycharmProjects/pythoncourse'))
