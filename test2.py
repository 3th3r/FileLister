import os

PATH=("/home/ego/TEST/")
crtFile=(PATH+"file.sync")

try:
    os.stat(PATH + ".sync")
except:
    os.mkdir(PATH + ".sync")

os.mknod(PATH+".sync/file.sync")
#open(r'/home/ego/TEST/.sync/test.sync')