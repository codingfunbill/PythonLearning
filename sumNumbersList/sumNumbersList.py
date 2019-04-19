#Guillermo Mejia
#04/18/19
#Program adds all items in list

itemList = []#Empty list
sum = 0

itemsInList = int(input("How many items are in this list? "))

for i in range(0,itemsInList):#Number of iterations
	item = int(input("Enter number: "))
	itemList.append(item)#Append item to list
	sum += item
	
print("The sum of all items in list is : ",sum)
	