import os
import time

file = '/home/ego/TEST/credential'
now = time.time()
age = now - os.path.getctime(file)

day = 3600 *24
hr = 3600

timeHrFl = float(age/hr)

print(now)
print(age)
print(timeHrFl)

