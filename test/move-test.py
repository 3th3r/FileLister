import os
import shutil

path1 = '/home/ego/TEST/move2/'
path2 = '/home/ego/TEST/move1/'
listobj = os.listdir(path1)

def moveFile (name, src, dest):

    if os.path.isdir(src + name) == True:
        shutil.move(src + name, dest)
    elif os.path.isfile(src + name) == True:
        shutil.move(src + name, dest + name)

for i in range(len(listobj)):
    moveFile(listobj[i],path1,path2)
    print(listobj[i])
