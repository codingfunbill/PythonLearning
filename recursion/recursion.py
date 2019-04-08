#Guillermo Mejia
#04/07/19
#Basic recursion function accepts a parameter

def recur(num):#single parameter
	if(num==0):#stops if equal to zero
		return num
	print(num)
	num * recur(num-1)
	
recur(5)