from distutils.file_util import move_file
from genericpath import isdir
import os
from posixpath import splitext

#Getting directory to clean
rootdir = input(r"Enter path of directory you want to clean. Eg: C:\xxxx\xxxx\dirToClean-")
files = os.listdir(rootdir)

#Function to create folders if folders don't exist
def createFolder(folderName,dir=rootdir):
    if not os.path.exists(f"{dir}\\{folderName}"):
        os.mkdir(f"{dir}\\{folderName}")

#Function to movefiles
def moveFiles(path,files):
    for file in files:
        os.replace(f"{rootdir}\\{file}",f"{rootdir}\\{path}\\{file}")

# Calling createFolder() function to create predefined folders
for x in ["Images","Videos","Documents","Compressed Files","Others"]:
    createFolder(x)

#Predefined format mapping
imgext = ['.jpg','.png','.jpeg','.gif','.raw']
vidext = ['.mp4','.mov','.mkv','.wmv']
docext = ['.txt','.pdf','.doc','.docx','.xls','.xlsx','.html','.csv']
compext = ['.7Z','.TAR.BZ2','.TAR.GZ','.RAR','.ZIP','.ZIPX','.TAR']

imgfile = []
vidfile = []
docfile = []
compfile = []
otherfiles = []

#Looping through once and placing them in correct list
for file in files:
    if isdir(f"{rootdir}\\{file}"):
        continue
    exten = os.path.splitext(file)[1].lower()
    if exten in imgext:
        imgfile.append(file)
    elif exten in vidext:
        vidfile.append(file)
    elif exten in docext:
        docfile.append(file)
    elif exten.upper() in compext:
        compfile.append(file)
    else:
        otherfiles.append(file)

#Calling moveFiles function to work on predefined folders and file formats
for x in [("Images",imgfile),("Videos",vidfile),("Documents",docfile),("Compressed Files",compfile)]:
    moveFiles(x[0],x[1])

#Getting a list of all other extensions available after moving files with predefined extensions
OfileExtSet = []
for file in otherfiles:
    exten = os.path.splitext(file)[1].lower()
    OfileExtSet.append(exten)
OFElist = list(set(OfileExtSet))

#Creating folders inside "Others" folder for extensions gatherd in previous step
for x in OFElist:
    x = str(x)
    x = x.strip('.')
    createFolder(x,f"{rootdir}\\Others")

#Moving files to there respective directories inside Other folder.
for file in otherfiles:
    exten = os.path.splitext(file)[1].lower()
    exten = str(exten).strip('.')
    temp = [file]
    moveFiles(f"Others\{exten}",temp)
