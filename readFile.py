#Guillermo Mejia
#04/26/19
#Reading files

f = open("textFile.txt","r")

#Reads whole file
#print(f.read())

#Reads first 5 characters of file
#print(f.read(5))

#Reads first line of file
#(f.readline())
#(f.readline())#Reads second line
selection = int(input("What line do you want to print? 1,2,3,4,or 5?"))
for i in range(5):
	if(i==(selection -1)):
		print("This is the line",f.readline())
	f.readline()
f.close()

f = open("textFile.txt","r")
counter = 0
for x in f:
	counter+=1
f.close()

print("The file has " , counter , "lines")