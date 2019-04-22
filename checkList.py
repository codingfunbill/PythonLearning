#Guillermo Mejia
#04/21/19
#Checks all elements in list for a specific value ranging from 1 to 100

#needed to use randint
from random import *


#generate numbers and add elements
#---Functions---
#Used to initialize a list
def initialize(list,q):
	for i in range(0,q):
		element = randint(1,100)#Generates random number for each element
		list.append(element)
	return list
#Used to check the list for a specific value in list
def check(list,q):
	count = 0
	#Ask user for a value to check 
	key = int(input("What number you looking for?1-100 "))
	for i in range(0,q):
		if(list[i] == key):
			count+=1
	return count#Return number of times(if any) value is found
#--------------


listIntegers =[]

#how many elements in list
quantity = int(input("How many elements in list?"))

initialize(listIntegers,quantity)#Initialize list

print("That number occured ",check(listIntegers,quantity),"times in list")
