# Datetime modules
import datetime

# current date and time
now = datetime.datetime.now()
print("current date and time:", now)

d = datetime.date(2024, 12 ,24)
print("Specific date:", d)

delta = now - datetime.datetime(2024, 8 ,1)
print("days since august 1, 2024:", delta.days)

# Formatting dates
formatted_date = now.strftime("%y-%m-%H:%M:%S")
print("Formatted date and time:", formatted_date)
