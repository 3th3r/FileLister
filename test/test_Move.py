import os
import shutil

os.chdir('//3g0-fnas/Media/Video/Movie')
for name in os.listdir("."):
    if name.endswith(".mkv"):
        print(name)
        os.mkdir('//3g0-fnas/Media/Video/Movie/'+name.replace(".mkv",""))
        shutil.move('//3g0-fnas/Media/Video/Movie/'+name, '//3g0-fnas/Media/Video/Movie/'+name.replace(".mkv", "")+ '/' + name)