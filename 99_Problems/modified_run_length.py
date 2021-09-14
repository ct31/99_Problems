
packList = ['a', 'a', 'b', 'c', 'd', 'e', 'e', 'f', 'a', 'a', 'a', 'q', 'q', 'r']
bufferList = []
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
             if len(bufferList) == 1:
                 runList.append(bufferList[0])
                 bufferList = []
                 element = sameChar
                 break
             else:
                myTuple = (len(bufferList), packList[element])
                runList.append(myTuple)
                bufferList = []
                element = sameChar
                break
     else:
             if len(bufferList) == 1:
                runList.append(bufferList[0])
             else: 
                yourTuple = (len(bufferList), packList[element])
                runList.append(yourTuple)
             
print(runList)