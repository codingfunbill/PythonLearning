#Guillermo Mejia
#04/23/19
#Program that uses different functions to sum items in a list


#----------FUNCTION DEFINITIONS---------------
#Function that uses a for loop to sum items in a list
def funcFor(list):
	sum=0#Initialize sum 
	for i in range(0,len(list)):
		sum+=list[i]#Sum of elements 
	return sum#Total sum of all elements 
	
#Function that uses a while loop to sum items in a list
def funcWhile(list):
	i=0#Iterator 
	sum=0#Initialize sum
	while(i < len(list)):
		sum+=list[i]#Sum of elements
		i+=1
	return sum#Total sum of all elements 
	
#Recursive function that sums items in a list
def rec(list, sum, i):#Three parameters. List, sum variable , and iterator
	if (i == len(list)):#Base case.Last element in list is reached
		return sum#This is total sum of all elements 
	sum += list[i]#Sum of elements 
	i+=1#Iterator
	return rec(list,sum,i)#Recursion 
#-----------------------------------------------

#List with 5 elements 
listOfNum=[2,5,8,10,3] 

print("The sum is ",funcFor(listOfNum))
print("The sum is ",funcWhile(listOfNum))
#One can initialize last 2 parameters to zero or just plug in zero for them in function 
print("The sum is ",rec(listOfNum,0,0))