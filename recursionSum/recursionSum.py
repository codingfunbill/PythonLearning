#Guillermo Mejia
#04/09/19
#Sum of numbers in range using recursion

print("This program will calculate the sum of consecutive numbers beginning at 1.")

#User inputs maximum number in range to sum here
lastNumber = int(input("Up to what number would you like to add?Please enter the number: "))
number = 0#Starting point of sum, or first number

def sum(num):
	if(num==lastNumber):#Base case
		return num
	return num + sum(num + 1)
	
print("The sum of all numbers from 1 to ",lastNumber,"is",sum(number))
	