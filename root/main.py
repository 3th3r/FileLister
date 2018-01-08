import pysftp
import os
import shutil
import configparser
import time

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read("/home/ego/TEST/credential")

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

pingR = False

rePATH = '/ethtorrent/downloads/complete/TEST/'              #remote path
lcPATH = '/home/ego/TEST/'                                   #local path
tmpPATH = lcPATH + '.tmp/'                                   #.tmp path, relative to lcPATH
syncPATH = lcPATH + '.sync/'
dlPATH = lcPATH + 'Downloads/'                               #downloads path, relative to lcPATH
dirList = os.listdir(lcPATH)                                 #list of all the file in lcPATH

syncList = ''                                                #initialise the sync varialbe, needed to compare if a file
                                                                        # .... have been already downladed
fileExist = 0                                                #initialize the varialbe needed to compare the sync list and
                                                                        # .... the file in rePATH dir



#################################################################################


##move file and folder,
              #name= name of the file, src = path of the source, dest = path of the destination

def moveFile (name, src, dest):

    if os.path.isdir(src + name) == True:
        shutil.move(src + name, dest)
    elif os.path.isfile(src + name) == True:
        shutil.move(src + name, dest + name)


##remove all file and directory in a given directory, path = path of the folder,
             # will delete all files and folder in this directory


def delInDIR (path):

    InLIST = os.listdir(path)
    crtOBJ = ''

    for i in range(len(InLIST)):

        crtOBJ = path+InLIST[i]

        if os.path.isdir(crtOBJ) == True:              #test if is a directory and delete it
            print(crtOBJ)
            shutil.rmtree(crtOBJ)
        elif os.path.isfile(crtOBJ) == True:           #test if is a file and delete it
            print(crtOBJ)
            os.remove(crtOBJ)



##Ping an adresse or an URL

def pingTest(url):
    response = os.system("ping -c 1 " + url)
    pingin = False

    # and then check the response...
    if response == 0:
        pingin = True
        #print(url, 'is up!')
    else:
        pingin = False
        #print(url, 'is down!')
    return pingin



##Age of of file from now

def fileAge(file):

    now = time.time()
    age = now - os.path.getctime(file)
    hr = 3600

    return float(age / hr)




##################################


with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        sftpLIST = sftp.listdir('')                        #list the files present in rePATH (DIR remote)
    
    ##Initialize the sync folder and object list
        #try if the .sync path / directory exist, otherwise create it
        try:
            os.stat(lcPATH + '.sync')
        except:
            os.mkdir(lcPATH + '.sync')
            
        try:
            os.stat(lcPATH + '.tmp')
        except:
            os.mkdir(lcPATH + '.tmp')

        syncList = os.listdir(lcPATH + '.sync')       #create the list of the file in .sync (DIR local)
        #print(sftpLIST)

        # test if the file is present in local or as already been downloaded
        for i in range(len(sftpLIST)):
            fileExist = 0

            if sftpLIST[i] in dirList:  # test if exist localy
                fileExist = 1
            elif (sftpLIST[i] + ".sync") in syncList:
                fileExist = 1  # test if already downloaded

            if fileExist == 1 :
                print(sftpLIST[i] + " : exist")  # if already downloaded or exist print "exist"

            # test if is a file them copy with a .tmp, and rename it
            elif sftp.isfile(sftpLIST[i]) == True:

                sftp.get(sftpLIST[i], tmpPATH + sftpLIST[i] + ".tmp", preserve_mtime=True)

                os.renames(tmpPATH + sftpLIST[i] + ".tmp", tmpPATH + sftpLIST[i])

                print(sftpLIST[i] + " : copied")
                os.mknod(syncPATH + sftpLIST[i] + ".sync")

            elif sftp.isdir(sftpLIST[i]) == True:

                sftp.get_r(sftpLIST[i], tmpPATH, preserve_mtime=True)

                print(sftpLIST[i] + " : folder copied")
                os.mknod(syncPATH + sftpLIST[i] + ".sync")

            moveFile(sftpLIST[i], tmpPATH, dlPATH)






