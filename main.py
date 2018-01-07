import pysftp
import os
import shutil

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

ftpIP = ''
ftpUSER = ''
ftpPWD = ''

rePATH = '/ethtorrent/downloads/complete/TEST/'              #remote path
lcPATH = '/home/ego/TEST/'                                   #local path
tmpPATH = lcPATH + '.tmp/'                                   #.tmp path, relative to lcPATH
dlPATH = lcPATH + 'Downloads/'                               #downloads path, relative to lcPATH
dirList = os.listdir(lcPATH)                                 #list of all the file in lcPATH
tmpPATH = lcPATH+'.tmp'

syncList = ''                                                #initialise the sync varialbe, needed to compare if a file
                                                                        # .... have been already downladed
fileExist = 0                                                #initialize the varialbe needed to compare the sync list and
                                                                        # .... the file in rePATH dir



#################################################################################


##move file and folder,
              #name= name of the file, src = path of the source, dest = path of the destination

def moveFile (name, src, dest):

    print(tmpPATH + name)

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
        print(sftpLIST)






#delInDIR("/home/ego/TEST/.tmp/new/")
