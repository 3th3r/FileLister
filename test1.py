import os
import shutil

lcPATH="/home/ego/TEST/"
tmpPATH=lcPATH+".tmp/"
dlPATH=lcPATH+"Downloads/"

dirLIST=os.listdir(tmpPATH)

#crt=""

print(tmpPATH)
print(lcPATH)
print(dlPATH)

for i in range(len(dirLIST)):
    #crt=tmpPATH + dirLIST[i]
    print(tmpPATH + dirLIST[i])
    #shutil.move(tmpPATH + dirLIST[i], dlPATH)
    if os.path.isdir(tmpPATH + dirLIST[i]) == True:
        shutil.move(tmpPATH + dirLIST[i], dlPATH)
    elif os.path.isfile(tmpPATH + dirLIST[i]) == True:
        shutil.move(tmpPATH + dirLIST[i], dlPATH + dirLIST[i])
