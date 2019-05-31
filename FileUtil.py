#!/usr/local/bin/python3
import pathlib,fnmatch,re
import os, sys
from datetime import datetime
from datetime import date

def DeleteOldFiles(path,maxagedays,pattern):
  print("path={0} days={1} pattern={2}".format(path,maxagedays,pattern))
  # define the path
  currentDirectory = pathlib.Path(path)

  for currentFile in currentDirectory.iterdir():  
    if fnmatch.fnmatch(currentFile, pattern):
#      if os.path.isdir(currentFile):
#        print("It is a Directory-{0}".format(currentFile))

      if os.path.isfile(currentFile):  
        print("It is a normal file-{0}".format(currentFile))  
        #look for timestamp in name
        regex = re.compile(r'(\d{2})(\d{2})(\d{2})\-(\d{5})\.tar\.gz') 
        match = regex.search(str(currentFile))
        if match:
          year = 2000 + int(match.group(1))
          month = int(match.group(2))
          day = int(match.group(3))
          timestring = match.group(4)
          
          datestring = "{0}/{1}/{2}".format(month,day,year)
          print('Date={0} Time={1}'.format(datestring,timestring))
          fromdate = date(year,month,day)
          currentdate = date.today()
          agedays = (currentdate-fromdate).days
          print("DAYS={0}".format(agedays))
          if agedays > maxagedays:
            print("File {0} is older than {1} days".format(currentFile,maxagedays)) 
            os.remove(currentFile) 
            
          
        