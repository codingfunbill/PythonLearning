#Guillermo Mejia
#Date: 4/6/2019
#Roll the dice program with user option to roll multiple times

#needed to use randint
from random import *

#user answer input if they would like to roll dice
choice ="y"

#or operator ,no parentheses, and both lower and capital y option
while choice =='y' or choice=='Y' :
	choice = input("Do you want to roll the dice? y/Y for yes: ")
	
	#no parentheses for if statement
	if choice=='y' or choice =='Y' :
		print("Rolling dice! ")
		print ("You got a ",randint(1, 6),"!")  