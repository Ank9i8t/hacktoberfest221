import os
from sys import prefix


# params: file extension and absolute path of directory
def list_files(file_extension, file_directory=os.getcwd()):
    dir_lists = os.listdir(file_directory)
    
    # filtering the list of all files to list of files that ends with the specified suffix
    return [x for x in dir_lists if x.endswith(f'.{file_extension}')]


print(list_files("txt", r"C:\enter\your\directory\here"))
print(list_files("png", r"C:\enter\your\directory\here"))
print(list_files("py", r"C:\enter\your\directory\here"))
print(list_files("json", r"C:\enter\your\directory\here"))
