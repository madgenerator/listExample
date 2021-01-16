testList = [1,2,3]
print(testList)

#append
testList.append(4)
print(testList)

#insert
testList.insert(1,1.5)
print(testList)

#delete
del testList[2]
print(testList)

#pop
popValue = testList.pop()
print(popValue)
print(testList)

#obj in list
print(5 in testList)
print(1 in testList)

#clear List
testList.clear()
print(testList)