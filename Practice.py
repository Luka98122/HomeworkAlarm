import json
from datetime import datetime
import time

def saveFunction (fileTo, Object):
    u = open (fileTo, 'wt')
    json.dump(Object, u)
    u.close()

def loadFunction (fileFrom):
    u = open (fileFrom, 'r')
    parsedJson = json.load(u)
    u.close()
    return parsedJson
    
nickName = "Triple Threat"
myList = []
MyDict = {
    "numbers" : myList,
    "Nickname" : nickName
}
for i in range(10):
    myList.append(i)

try:
    MyDict = loadFunction('File.txt')
except FileNotFoundError :
    u = open('File.txt', 'wt')
    saveFunction('File.txt', myList)
    u.close()

for i in range (10):
    MyDict['numbers'][i] = MyDict['numbers'][i] * 2
saveFunction('File.txt', MyDict)
print(MyDict)
