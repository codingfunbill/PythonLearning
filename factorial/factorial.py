#Guillermo Mejia
#04/07/19
#Factorial function using recursion

def recur(num):#single parameter
	if(num==0):#stops if equal to zero,base case 
		return 1
	print(num)
	return num * recur(num-1)
number = int(input("Input a number to get it's factorial: "))	
print("The factorial of ",number," is ",recur(number))
