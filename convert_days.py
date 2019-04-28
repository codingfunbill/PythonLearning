#Guillermo Mejia
#Day converter program

daysInput = int(input("How many days?"))
years = daysInput//365
months = daysInput%365//30
weeks = daysInput%365%30
days = weeks%7
test = daysInput%365%30%7

print(years," years.")
print(months," months.")
print(weeks," weeks.")
print(days," days.")
print(test)