#Guillermo Mejia
#04/20/19
#Display largest number from list using functions

#---Functions---
def initialize(list,q):
	for i in range(0,q):
		element = int(input("Enter a number: "))
		list.append(element)
	return list

def check(list,q):
	largest = list[0]
	for i in range(0,q):
		if(list[i] > largest):
			largest = list[i]
	return largest
#--------------

listNumbers =[]

quantity = int(input("How many elements in list?"))

#Initialize list
listNumbers = initialize(listNumbers,quantity)

#iterate through list to find max
max = check(listNumbers,quantity)	
	
print("The largest number in this list is ",max)
		
	