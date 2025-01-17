#CS161 Week 3 Python
#Take input, print hello
name = input ("What is your name? ")
print(f"Hello, {name}!")

#Cannot add an integer to string; so add int()
age = int(input("What is your age? "))
print (age + 5)

#Ask user to add to their current age
add_age = int(input("Add a number of years to your age: "))
#Combine current age with their contribution
new_age = age + add_age

#Concatenate with str()
print ("In " + str(add_age) + " years you will be " + str(new_age) + "!")



#Ask for hours worked and wage
hours_worked = float(input("How many hours did you work this week? "))
wage = float(input("Enter your hourly wage (without the $): "))

#Multiply to get weekly pay
before_tax_pay = hours_worked * wage
#Calculate salary, 40 hours * 50 weeks (assuming full time)
salary = wage * 2000

#if and elif to determine which tax bracket
if 11600 >= salary:
    tax = 0.1
elif 47150 >= salary:
    tax = 0.12
elif 100525 >= salary:
    tax = 0.22
elif 191950 >= salary:
    tax = 0.24
elif 243725 >= salary:
    tax = 0.32
elif 609350 >= salary:
    tax = 0.35
else:
    tax = 0.37

#Calculate annual tax and net income
yearly_tax = salary * tax
net_salary = salary - yearly_tax

#Print results with strings, this assumes full time work no matter what
print("Your gross pay this week is $" + str(before_tax_pay) + "\n" +
      " Your estimated annual gross pay will be $"  + str(salary) + "\n" +
      " Your yearly tax will be $" + str(yearly_tax)  + "\n"
      " Your net annual income after taxes is $" + str(net_salary))


