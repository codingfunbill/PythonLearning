#Guillermo Mejia
#4/16/19
#Program prompts for five integers and calculates the sum of those that
#are positive. 

sum = 0

for i in range(0,5):
	number = int(input("Please enter number: "))
	if(number > 0):
		sum+=number#Adds positive numbers
	
print("Sum of positive numbers is ",sum)