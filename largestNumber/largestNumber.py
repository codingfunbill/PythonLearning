#Guillermo Mejia
#4/20/19
#Display largest number from list

listNumbers =[]

print(len(listNumbers))

quantity = int(input("How many elements in list?"))
#largest = 0#Stores largest number in the list

#for i in range(0,quantity)
element = int(input("Enter a number: "))
listNumbers.append(element)
largest = listNumbers[0]
#largest = listNumbers[0]

for i in range(0,quantity-1):
	element = int(input("Enter a number: "))
	if(element > largest):
		largest = element
	listNumbers.append(element)
		
print("The largest number in this list is ",largest)
		
	