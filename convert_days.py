daysInput = int(input("How many days?"))
years = daysInput//365
months = daysInput%365/30
weeks =  months/7
days = weeks%7

print(years," years.")
print(months," months.")
print(weeks," weeks.")
print(days," days.")