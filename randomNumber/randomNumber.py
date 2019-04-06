from random import *

choice ="y"
while choice =='y' or choice=='Y' :
	choice = input("Do you want to roll the dice? y/Y for yes: ")
	if(choice=='y' or choice =='Y') :
		print("Rolling dice! ")
		print ("You got a ",randint(1, 6),"!")  