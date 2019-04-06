number = 0
sum = 0
choice = 0
product = 1
average = 0
counter = -1
while number != 9999 :
	number = int(input("Please input a number, enter 9999 to stop: "))
	sum+=number
	product*=number
	if number == 9999 :
		sum-=9999
		product/=9999
	counter+=1
	
print("For sum of these numbers enter 1")
print("For product of these numbers enter 2")
print("For sum and product of these numbers enter 3")

choice = int(input("Please make a selection: 1,2,3: "))
if(choice == 1) :
	print("Sum is ",sum)
elif(choice == 2) :
	print("Product is ",product)
elif(choice == 3) :
	print("Sum is ",sum)
	print("Product is ",product)
else :
	print("You didn't select a choice ")