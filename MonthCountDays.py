# input month name 
month_name = input("Enter the month name: ").lower()
if month_name == "january" or month_name =="march" or month_name == "may" or month_name == "july" or month_name == "august"or month_name == "october" or month_name == "december": 
    days =  31
elif month_name == "april" or month_name == "june" or month_name == "september" or month_name == "november":
    days = 30
elif month_name == "february":
    days = 28 
else:
    days = "Invalide month name"
print(F"The number of days in {month_name.capitalize()} is : {days}")
