#Guillermo Mejia
#Date: 04/06/2019
#Average of numbers entered by user

number = 0
sum = 0
average = 0
counter = -1
while number != 9999 :
	number = int(input("Please input a number, enter 9999 to stop: "))
	sum+=number
	if number == 9999 :
		sum-=9999
	counter+=1

average = sum / counter

print("Average is ",average)