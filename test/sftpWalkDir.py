import pysftp
import configparser


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read(r'C:\Users\3g0\Desktop\credential')

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

rePATH = '/ethtorrent/downloads/complete/TEST/'

wtcb = pysftp.WTCallbacks()

with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    with sftp.cd(rePATH):                             #go to the directory rePATH
        sftp.walktree(rePATH,fcallback=wtcb,dcallback=wtcb.dir_cb(),ucallback=wtcb.unk_cb())
        print(len(wtcb.flist))
        for fpath in wtcb.flist:
            print(fpath)
sftp.close()