import pysftp
import configparser


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read('/home/local1/TEST/credential')

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

rePATH = '/ethtorrent/downloads/complete/TEST'

wtcb = pysftp.WTCallbacks()

with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    sftp.walktree(rePATH, wtcb.file_cb, wtcb.dir_cb, wtcb.unk_cb, recurse=True)

    for entry in sftp.listdir(rePATH)
        pathname = pos