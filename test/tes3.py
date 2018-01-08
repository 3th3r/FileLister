import os

rePATH="/ethtorrent/downloads/complete/TEST/" # remote path
lcPATH="/home/ego/TEST/" #local path
dirList=os.listdir(lcPATH)

syncList = os.listdir(lcPATH + ".sync")

#print(rePATH)
#print(lcPATH)
print(syncList)
