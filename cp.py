import time

print "Copy Paste initialized.....\n"


dataFile = open("C:\\Users\\Rahul\\Desktop\\py.hp\\data.txt",'r')

dataFile.seek(0)

dataList = dataFile.readlines()


opFile = open("C:\\Users\\Rahul\\Desktop\\py.hp\\op.txt",'w+')


for n in dataList:


	if n.startswith('a'):

		opFile.write(n)
		


opFile.seek(0)

opList = opFile.readlines()

print 'Data Copy pasted:\n', opList


print '\nCopy Paste Successfully Completed!!'


opFile.close()

dataFile.close()


time.sleep(5)