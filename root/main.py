import pysftp
import os
import shutil
import configparser
import time
import datetime
import re

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

maxAge = 7                                                   #define the maximun of a file to be downloaded, older than
                                                                        # "maxAge" (in days) won't be downlaoded

syncList = ''                                                #initialise the sync varialbe, needed to compare if a file
                                                                        # .... have been already downladed
fileExist = False                                            #initialize the varialbe needed to compare the sync list and
                                                                        # .... the file in rePATH dir
toOld = False                                                #initialize the needed to compare if older than maxAge
now = time.time()

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





##################################


with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        sftpLIST = sftp.listdir('')                        #list the files present in rePATH (DIR remote)

        ##Time difference between server and now

        sftATTRlist = sftp.listdir_attr('')
        maxAgeSec = maxAge*86400                         #convert days in second, easier to handle time compare

        tmpATTR = str(sftATTRlist)
        tmpATTR = tmpATTR.split(',')

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
            fileExist = False
            toOld = False

            if sftpLIST[i] in dirList:  # test if exist localy
                fileExist = True
            elif (sftpLIST[i] + ".sync") in syncList:
                fileExist = True  # test if already downloaded

            rtimeTmp = re.findall(r'mtime=\w+',str(tmpATTR[i]) )
            rtime = re.findall( r'\d+', str(rtimeTmp[0]) )
            deltaTime = datetime.timedelta(seconds=now - int(rtime[0]))



            if deltaTime.total_seconds() > maxAgeSec:
                toOld = True


            if fileExist == True:
                print(sftpLIST[i] + " : exist")                          # if already downloaded or exist print "exist"

            # test is file or dir is than maxAge
            elif toOld == True:
                print(sftpLIST[i] + ' : older than ' + str(maxAge) + ' days')
            # test if is a file them copy with a .tmp, and rename it
            elif sftp.isfile(sftpLIST[i]) == True:

                sftp.get(sftpLIST[i], tmpPATH + sftpLIST[i] + ".tmp", preserve_mtime=True)

                os.renames(tmpPATH + sftpLIST[i] + ".tmp", tmpPATH + sftpLIST[i])

                print(sftpLIST[i] + " : copied")
                os.mknod(syncPATH + sftpLIST[i] + ".sync")
            # test if is a dir them copy with a .tmp, and rename it
            elif sftp.isdir(sftpLIST[i]) == True:

                sftp.get_r(sftpLIST[i], tmpPATH, preserve_mtime=True)

                print(sftpLIST[i] + " : folder copied")
                os.mknod(syncPATH + sftpLIST[i] + ".sync")

            moveFile(sftpLIST[i], tmpPATH, dlPATH)






