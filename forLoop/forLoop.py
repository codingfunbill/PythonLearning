n = 0
sum = 0
n = int(input("Please enter a number: "))
i = 0

for i in range(0 , n)  :
	i+=1
	print(i)
	sum+=i
	
print("The sum of numbers from 1 to ",n)
print("is ",sum)