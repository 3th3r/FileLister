import os
import shutil

path1 = r'E:\Telecharger\MobaXterm_Portable_v10.4\CygUtils.plugin'
path2 = r'E:\test'

shutil.copy(path1,path2)
print(path1)
print(path2)
