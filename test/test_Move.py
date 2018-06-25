import os
import shutil

PATH='//3g0-fnas/Media/Video/AnimeMovie/Walt Disney'
PATH2=PATH+'/'

os.chdir(PATH)
for name in os.listdir("."):
    if name.endswith(".mkv"):
        print(name)
        os.mkdir(PATH2+name.replace(".mkv", ""))
        shutil.move(PATH2+name, PATH2+name.replace(".mkv", "")+ '/' + name)