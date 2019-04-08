#Guillermo Mejia
#04/07/19
#Exponent program using recursion.

def exponent(base,power):
	if(power==0):#base case
		return 1#cannont return 0 because product result will be 0
	return base * (exponent(base,power-1))
	
number = int(input("Enter a number: "))
pow = int(input("Enter a power: "))

print(number,"to the power of",pow,"is",exponent(number,pow))