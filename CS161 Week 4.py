#Week 4 Python

def average(num1, num2,num3):
 '''Function that returns the average of 3 numbers'''
 return (num1 + num2 + num3) / 3

print(average (1,2,3))
print(average(21,30,90))
#print(num1)
#Function does not run with print statements first because python reads
#files top to bottom and the function hasn't been defined
#num1 will not print because it's a local variable, it only exists with the function running

def dogs_age(age):
    '''This function calculates dog's age in human years'''
    return (24 + (age - 2) *4)

test = [90, 3, 9, 5]

for age in test:
    human = dogs_age(age)
    print(f"{age} dog years is equivalent to {human} human years.")


def value(car, price, years):
    '''This function calculates the value of the car
    in x years dependent on the make'''
    if car == "german":
        return price * (0.95 ** years)
    elif car == "japanese":
        return price * (0.93 ** years)
    elif car == "italian":
        return price * (1.05 ** years)

car = "german"
original = 3000
years = 20

car_value = value(car, original, years)
print(f"The value of a ${original} {car} car will be ${car_value:.2f} after {years} years.")

def canine_life_length(canine_age):
    '''This function calculates canine years into human years'''
    return (24 + (canine_age - 2) * 4)

canine_name = input("What is your dog's name? ")
canine_age = int(input(f"How old is {canine_name}? "))
human_age = canine_life_length(canine_age)
print(f"Your dog {canine_name} is {human_age} human years old.")

def cone_price(scoops):
    """This function calculates price of ice cream cone based on number of scoops"""
    return scoops * 1.15 + 2.25

print("Ice cream cone price calculator:")
scoops = int(input("How many scoops would you like? "))

price = cone_price(scoops)

print(f"A {scoops} scoops cone will cost ${price}.")

