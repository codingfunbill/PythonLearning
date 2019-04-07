

def recur(num):
	if(num==0):
		return num
	print(num)
	recur(num-1)
	
recur(5)