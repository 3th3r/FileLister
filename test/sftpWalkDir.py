import pysftp
import configparser


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read('/home/local1/TEST/credential')

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

rePATH = '/ethtorrent/downloads/complete/'

wtcb = pysftp.WTCallbacks()

with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    sftp.walktree( rePATH, fcallback=wtcb.dir_cb, dcallback=wtcb.dir_cb, ucallback=wtcb.unk_cb )
    print(len(wtcb.flist))
    for fpath in wtcb.flist:
        print(fpath)
sftp.close()