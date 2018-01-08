import pysftp
import configparser

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
config = configparser.ConfigParser()
config.read("/home/local1/TEST/credential")

ftpIP = config.get('configuration','ip')
ftpUSER = config.get('configuration','username')
ftpPWD = config.get('configuration','password')

rePATH = '/ethtorrent/downloads/complete/TEST/'

with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        sftpLIST = sftp.listdir('')
        print(sftpLIST)