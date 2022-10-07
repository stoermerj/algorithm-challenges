"""
https://www.101computing.net/mode-algorithm-using-a-hash-table/
find the mode
"""

import random

rawList = []
for i in range(0,20):
  rawList.append(random.randint(0,10))
print(rawList)

z = []
for x,y in enumerate(rawList):
    t = rawList.count(y)
    z.append(t)
indexRawList = z.index(max(z))

#this is the mode
print(rawList[indexRawList])