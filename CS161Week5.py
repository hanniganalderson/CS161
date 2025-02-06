#CS161 Week 5
import requests
import psutil

#Ask for an integer from user
number = int(input("Enter a number: "))
#Determine if number can be divided by 5 with no remainder
if number % 5 == 0:
    print ("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

#Ask user to input a state, lower() for ease
state = input("Enter a US state: ").lower().strip()
#If statements matching state names to print capitals
if state == "oregon":
    print("The capital of Oregon is Salem")
elif state == "florida":
    print("The capital of Florida is Tallahassee")
elif state == "georgia":
    print("The capital of Georgia is Atlanta")
elif state == "idaho":
    print("The capital of Idaho is Boise")
elif state == "illinois":
    print("The capital of Illinois is Springfield")
elif state == "indiana":
    print("The capital of Indiana is Indianapolis")
else:
    print("I do not know that one")

capitals = {
    "Oregon": "Salem",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis"
}
#Get input, no spaces, title case matches dictionary
state = input("Enter a US state: ").strip().title()
capital = capitals.get(state, "I do not know that one")
print(f"The capital of {state} is {capital}.")

#Match case approach
state = input("Enter a US state: ").strip().title()

match state:
    case "Oregon":
        print("The capital of Oregon is Salem.")
    case "Florida":
        print("The capital of Florida is Tallahassee.")
    case "Georgia":
        print("The capital of Georgia is Atlanta.")
    case "Idaho":
        print("The capital of Idaho is Boise.")
    case "Illinois":
        print("The capital of Illinois is Springfield.")
    case "Indiana":
        print("The capital of Indiana is Indianapolis.")
    case _:
        print("I do not know that one.")

#Public pool entrace prices

def pool_prices(age):
    """Function determines pool entrance price based on age
    Parameters:
    age (as an integer): age of person
    Returns:
    integer, the admission price in dollars
    """
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

person_age = int(input("Enter your age: "))
print(f"Price to enter is {pool_prices(person_age)}")

#URL and substring to look for
url = "http://coccbobcat.com"
substring = "160"

try:
    response = requests.get(url)
    amount = response.text.count(substring)
    print(f'The substring "{substring}" appears {amount} times in the HTML source of {url}.')
#Handles errors
except:
    print("Error")

#Determines length of list of all currently running process ids (PIDs!)
number_processes = len(psutil.pids())
#Print the number
print(f"Number of running processes: {number_processes}")