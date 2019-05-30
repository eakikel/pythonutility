import pathlib
import os, sys

# define the path
currentDirectory = pathlib.Path('.')

for currentFile in currentDirectory.iterdir():  
    if os.path.isdir(currentFile):
      print("It is a Directory-{0}".format(currentFile))

    if os.path.isfile(currentFile):  
      print("It is a normal file-{0}".format(currentFile))  