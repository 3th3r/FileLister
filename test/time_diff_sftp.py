import pysftp
import time
import configparser
import re
import datetime


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read("/home/ego/TEST/credential")

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

rePATH = '/ethtorrent/downloads/complete/TEST/'              #remote path


with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):
        sftpLIST = sftp.listdir('')

        now = time.time()

        tutu=sftp.listdir_attr('')
        toto=str(tutu)
        toto = toto.split(',')
        tata = re.findall(r'mtime=\w+',str(toto[1]))
        titi = re.findall( r'\d+', str(tata[0]) )

        rtime = int(titi[0])
        #dif = now - rtime

        modTime = datetime.datetime.fromtimestamp(rtime)
        modTime2 = datetime.datetime.fromtimestamp(now)
        delta = datetime.timedelta(seconds=(now-rtime))
        #deltaSec = datetime.timedelta.seconds(delta)
        #datetime.timedelta.seconds


        #print(toto[0])
        #print(tutu[0])
        #print(tata)
        print(rtime)
        print(now)
        print(modTime)
        print(modTime2)
        print(delta)
        print(type(delta))
        print(delta.total_seconds())