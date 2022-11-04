from fileinput import filename
import os

# from macpath import dirname

# print(os.getcwd())
# os.chdir("/Users/abidinm/Desktop/")
# print(os.getcwd())
for dirpath, dirnames, filenames in os.walk("/Users/abidinm/Desktop/"):
    print("currentPath", dirpath)
    print("dirnames", dirnames)
    print("filenames", filenames)
    print()
