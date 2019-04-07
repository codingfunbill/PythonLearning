#Guillermo Mejia
#04/07/19
#Function that prints 'Hello World', and function that returns product of 2 numbers

def func():
	print("Hello World from function!")
	
func()

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

def multiply(a,b):
	return a * b 
	
multi = multiply(num1,num2)

print("The product of both numbers is ",multi)
