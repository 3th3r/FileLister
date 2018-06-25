import pysftp
import configparser
import os


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cred = configparser.ConfigParser()
cred.read('/home/local1/TEST/credential')

ftpIP = cred.get('credential','ip')
ftpUSER = cred.get('credential','username')
ftpPWD = cred.get('credential','password')

rePATH = '/ethtorrent/downloads/complete/TEST/'
locPATH = '/home/local1/TEST/tmpFiles/'

def put_r(self, localpath, remotepath, confirm=True, preserve_mtime=False):
    """Recursively copies a local directory's contents to a remotepath

    :param str localpath: the local path to copy (source)
    :param str remotepath:
        the remote path to copy to (target)
    :param bool confirm:
        whether to do a stat() on the file afterwards to confirm the file
        size
    :param bool preserve_mtime:
        *Default: False* - make the modification time(st_mtime) on the
        remote file match the time on the local. (st_atime can differ
        because stat'ing the localfile can/does update it's st_atime)

    :returns: None

    :raises IOError: if remotepath doesn't exist
    :raises OSError: if localpath doesn't exist
    """
    #self._sftp_connect()
    wtcb = pysftp.WTCallbacks()
    cur_local_dir = os.getcwd()
    os.chdir(localpath)
    walktree('.', wtcb.file_cb, wtcb.dir_cb, wtcb.unk_cb)
    # restore local directory
    os.chdir(cur_local_dir)
    for dname in wtcb.dlist:
        if dname != '.':
            pth = reparent(remotepath, dname)
            if not self.isdir(pth):
                self.mkdir(pth)

    for fname in wtcb.flist:
        head, _ = os.path.split(fname)
        if head not in wtcb.dlist:
            for subdir in path_advance(head):
                if subdir not in wtcb.dlist and subdir != '.':
                    self.mkdir(reparent(remotepath, subdir))
                    wtcb.dlist = wtcb.dlist + [subdir, ]
        src = os.path.join(localpath, fname)
        dest = reparent(remotepath, fname)
        # print('put', src, dest)
        self.put(src, dest, confirm=confirm, preserve_mtime=preserve_mtime)



with pysftp.Connection(ftpIP, username=ftpUSER, password=ftpPWD, cnopts=cnopts) as sftp:
    put_r(locPATH,rePATH,False,False)