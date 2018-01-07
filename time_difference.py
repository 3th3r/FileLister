from os import path
from datetime import datetime, timedelta

file = '/home/ego/Vidéos'
timeDif = 5

nDayAgo = datetime.now() - timedelta(days=timeDif)
filetime = datetime.fromtimestamp(path.getctime(file))

if filetime < nDayAgo:
  print("File is more than " + str(timeDif) + " days old")
else:
  print("files is not more than " + str(timeDif) +" days old")