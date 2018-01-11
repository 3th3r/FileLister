import os
import shutil

PATH = r'E:\Telecharger'
TESTP = r'E:\test'

def moveFile (name, src, dest):

    if os.path.isdir(src + name) == True:
        shutil.move(src + name, dest)
    elif os.path.isfile(src + name) == True:
        shutil.move(src + name, dest + name)

for root, dirs, files in os.walk(PATH, topdown=False):
    crtDir = root.replace(PATH,'')
    #print('root : ',root)
    #print('crtDir : ',crtDir)

    if crtDir != '':
        try:
            os.stat(TESTP+crtDir)
        except:
            os.mkdir(TESTP+crtDir)
            #print(TESTP+crtDir,' : dir created')

    for file in files:
        shutil.copy(PATH+crtDir+'\\'+file,TESTP+crtDir)
        #print('     ',PATH + crtDir + '\\'  + file)
        #print('path = ',PATH)
        #print('crtDire = ', crtDir)
        print(file)

    #print('\n')
    #print('dir : ',dirs)
    #print('files : ',files)


