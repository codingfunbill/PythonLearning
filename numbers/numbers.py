#Guillermo Mejia
#Program accepts 3 numbers and displays smallest and largest of the 3
n = 0
n = int(input("Please enter a number: "))
small = n 
large = 0

i = 0

for i in range(0 , 2)  :
	n = int(input("Please enter a number: "))
	if n > large :
		large = n
	if n < small :
		small = n
	
print("Small ",small)
print("Large ",large)