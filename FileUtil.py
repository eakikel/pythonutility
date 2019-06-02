#!/usr/local/bin/python3
import pathlib,fnmatch,re
import os, sys
from datetime import datetime
from datetime import date
#     Parameter Passed
#     First Parameter-  path to directory where we want to delete files
#     Second Parameter- Number of old to keep
#     Third Parameter-  Pattern of Files to lookfor
#                       Example: local-userdb*.tar.gz
def DeleteOldFiles(path,maxage,pattern):
  result = ("path={0} maxage={1} pattern={2}\n".format(path,maxage,pattern))
  # define the path
  dirs = os.listdir( path )

# loop thru files and sub-directories in the directory
  for currentFile in sorted(dirs):  
  #    print(currentFile)
    # Check for patter match of File name
    if fnmatch.fnmatch(currentFile, pattern):
      pathplusfilename = path + currentFile
      # Check if name is file and not sub directory
      if os.path.isfile(pathplusfilename):  
        #look for timestamp in name
        regex = re.compile(r'(\d{2})(\d{2})(\d{2})\-(\d{5})\.tar\.gz') 
        match = regex.search(str(currentFile))
        if match:
          year = 2000 + int(match.group(1))
          month = int(match.group(2))
          day = int(match.group(3))
          timestring = match.group(4)
        
          datestring = "{0}/{1}/{2}".format(month,day,year)
  #          print('Date={0} Time={1}'.format(datestring,timestring))
          fromdate = date(year,month,day)
          currentdate = date.today()
          # calculate difference between file date and today
          agedays = (currentdate-fromdate).days
  #          print("DAYS={0}".format(agedays))
          if agedays > maxage:
            result = result + ("Deleting {0} which is {1} days old\n".format(currentFile,agedays,maxage)) 
            os.remove(pathplusfilename) 
  return result
            
       