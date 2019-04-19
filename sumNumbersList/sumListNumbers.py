#Guillermo Mejia
#04/18/19
#Program adds all items in list of 5 integers

itemList = [13,20,7,21,3]
sum = 0

for i in range(0,len(itemList)):
	sum += itemList[i]#Add each item in list
	
print("The sum of all items in list is : ",sum)