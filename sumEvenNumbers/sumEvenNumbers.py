#Guillermo Mejia
#04/08/19
#Recursion function sum of even numbers 2 to a maximum even number entered by user

number = 0
lastEven = 0#Last even number to be added

print("This program will sum even numbers from 2 to designated maximum even number.")
lastEven = int(input("Please enter a designated maximum even number: "))#User inputs maximum even number

def sumEven(num):
	maxEven = lastEven
	if(num==maxEven):#base case, if even number equals max even number in range
		return num
	return num + sumEven(num + 2)#Keep adding 2 until max even number is reached

	
print("The sum of even numbers from 2 to ",lastEven,"is",sumEven(number))