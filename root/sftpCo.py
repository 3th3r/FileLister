import pysftp
import os
import configparser

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
config = configparser.ConfigParser()
config.read("/home/local1/TEST/credential")

ftpIP = config.get('configuration','ip')
ftpUSER = config.get('configuration','username')
ftpPWD = config.get('configuration','password')

rePATH="/ethtorrent/downloads/complete/TEST/"              #remote path
lcPATH="/home/ego/TEST/"                                   #local path
dirList=os.listdir(lcPATH)                                 #list of all the file in lcPATH
tmpPATH=lcPATH+".tmp"
syncList=""                                                #initialise the sync varialbe, needed to compare if a file
                                                                        # .... have been already downladed
fileExist=0                                                #initialize the varialbe needed to compare the sync list and
                                                                        # .... the file in rePATH dir




#connect to the server through sftp, using credential !!!!! need to create a credential file, for more security.

with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        tmp = sftp.listdir('')                        #list the files present in rePATH (DIR remote)

        #try if the .sync path / directory exist, otherwise create it
        try:
            os.stat(lcPATH + ".sync")
        except:
            os.mkdir(lcPATH + ".sync")

        syncList = os.listdir(lcPATH + ".sync")       #create the list of the file in .sync (DIR local)


        #test if the file is present in local or as already been downloaded
        for i in range(len(tmp)):
         fileExist=0

         if tmp[i] in dirList:                        #test if exist localy
             fileExist=1
         elif (tmp[i]+".sync") in syncList:
             fileExist=1                              #test if already downloaded


         if fileExist==1:
             print(tmp[i] +" : exist")                #if already downloaded or exist print "exist"
         #test if is a file them copy with a .tmp, and rename it
         elif sftp.isfile(tmp[i]) == True:
             sftp.get(tmp[i], lcPATH + tmp[i] + ".tmp", preserve_mtime=True)
             os.renames(lcPATH + tmp[i] + ".tmp", lcPATH + tmp[i])
             print(tmp[i] + " : copied")
             os.mknod(lcPATH + ".sync/" + tmp[i] + ".sync")
         elif sftp.isdir(tmp[i]) == True:
             sftp.get_r(tmp[i], lcPATH, preserve_mtime=True)
             os.mknod(lcPATH + ".sync/" + tmp[i] + ".sync")
             print(tmp[i]+" : folder copied")
