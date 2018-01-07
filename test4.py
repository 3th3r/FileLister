import pysftp
import os

rePATH="/ethtorrent/downloads/complete/TEST/"
lcPATH="/home/ego/TEST/"

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection('', username='', password='', cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        tmp = sftp.listdir('')
        #print(tmp)
        #print(lcPATH)
        #sftp.get_d(rePATH + tmp[0], lcPATH, preserve_mtime=True)
        for i in range(len(tmp)):
            #print(sftp.isdir(tmp[i]))
            #print(tmp[i])
            if sftp.isdir(tmp[i]) == True:
                print(tmp[i]+" : is a directory")
            elif sftp.isfile(tmp[i]) == True:
                print(tmp[i]+" : is a file")
