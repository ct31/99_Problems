
packList = ['a', 'a', 'b', 'c', 'd', 'e', 'e', 'f', 'a', 'a', 'a', 'q', 'q', 'r']
bufferList = []
newList = []
runList = []

element = 0
sameChar = 0
bounds = len(packList) - 1

while sameChar <= bounds:

     bufferList.append(packList[element])
     sameChar = element + 1

     while sameChar <= bounds:

         if packList[element] == packList[sameChar]:
             bufferList.append(packList[sameChar])
             sameChar = sameChar + 1 
         else: 
            # newList.append(bufferList.copy())
            newList.append(bufferList)
            myTuple = (len(bufferList), packList[element])
            runList.append(myTuple)
            bufferList = []
            element = sameChar
            break
     else:
             yourTuple = (len(bufferList), packList[element])
             runList.append(yourTuple)
             newList.append(bufferList)
print(runList)