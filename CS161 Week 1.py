#CS161 Week 1
#Assign variables
pet_type = "dog"
pet_name = "Mellie"
#Print sentence
print (f"I have a {pet_type} named {pet_name}.")

#Assign variables to inputs
first_name = input("Enter your first name: ")
age = int(input("Enter your current age: "))
annual_savings = int(input("Enter your yearly savings: "))

#Calculate the 3 scenarios:
#Add 10 years to age
in_ten_years = age + 10
#Multiply savings by 5
if_you_save = annual_savings * 5
#Divide savings by 12
average_monthly_savings = annual_savings / 12

#Print out results
print(f"Hello {first_name}! You are currently {age} years old.")
print(f"In 10 years, you will be {in_ten_years} years old.")
print(f"If you save {annual_savings} per year, in 5 years you will have ${if_you_save}.")
print(f"Your average monthly savings is ${average_monthly_savings}.")

#Import libraries
import calendar
from datetime import datetime

#Getting the current year and month
year = datetime.now().year
month = datetime.now().month
#Calculate the number of days in current month
days_in_month = calendar.monthrange(year, month)[1]
#86,400 seconds in a day, so multiply with days in month, print
print(f"The number of seconds in the current month is {days_in_month * 86400}.")

#Integer input for eggs
eggs = int(input ("Enter the number of eggs: "))

#Calculate quantity of dozens and how many leftover
egg_dozens = eggs // 12
eggs_leftover = eggs % 12
#Print statement with f string
print(f"This makes {egg_dozens} dozen eggs with {eggs_leftover} left over.")
