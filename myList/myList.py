#Guillermo Mejia
#04/17/19
#Program that asks a user for numbers to input into an array and prints them.

#Empty list
my_list = []

#Number of elements specified by user
numElements = int(input("Number of elements:"))

#Range of iteration
for i in range (0,numElements):
	element = int(input("Enter integer: "))#Input element integer
	my_list.append(element)#Append element to list
	
print("You entered the following elements.")
for j in range (0,numElements):
	print(my_list[j])
	
