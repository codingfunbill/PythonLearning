#Guillermo Mejia
#04/16/19
#Program that prints numbers 1 to 100. If number is multiple of 3 it prints 'Fizz'.
#If number is multiple of 5 it prints 'Buzz'.If multiple of both 3 and 5 it prints 'FizzBuzz'

for i in range(1,101):
	if(i % 3 == 0 and i % 5 == 0):#If multiple of both 3 and 5
		print("FizzBuzz")
	elif(i % 5 == 0):#If multiple of 5
		print("Buzz")
	elif(i % 3 == 0):#If multiple of 3
		print("Fizz")
	else:
		print(i)