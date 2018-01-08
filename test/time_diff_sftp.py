import pysftp
import time
import configparser


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
        #age = now - os.path.getctime('')
        #hr = 3600

        #print(sftp.listdir_attr('LBC'))
        tutu=sftp.listdir_attr('')
        toto=str(tutu)
        toto = toto.split(',')

        #print(tutu)
        #print(type(tutu))
        print(tutu[0])
        print(toto[0])



        #for toto in tutu:
        #    print(toto)

        #for attr in sftp.listdir_attr():
        #    print(attr)
        #    #print(attr.size)