#Guillermo Mejia
#04/10/19
#Guessing a number game

#needed to use randint
from random import *

#generate random number from 1 to 100
number = randint(1,100)
guessNumber = 0
count = 0#Counts how many attempts to guess correctly

while(guessNumber!=number):
	#user inputs a guess number
	guessNumber = int(input("Please guess the correct number from 1 to 100: "))
	count+=1
	if(guessNumber!=number and guessNumber > number):
		print("Incorrect, try a lower number")
	elif(guessNumber!=number and guessNumber < number):
		print("Incorrect, try a higher number")
	elif(guessNumber==number):
		print("Congratulations!",number,"was the correct number.")
		print("You got it right after ",count,"attempts.")
