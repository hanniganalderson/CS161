#CS161 Week 7

#Ask for user input lower and higher
low = int(input("Enter the lower number: "))
high = int(input("Enter the higher number: "))
print(f"The even numbers between {low} and {high} are: ")
for num in range(low, high + 1): #+1 to include the high number
    if num % 2 == 0: #If no remainder when dividing by 2, even integer
        print(num)

positive_int = int(input("Enter a positive integer: "))
if positive_int<=0: #Discard negative integers
    print("Enter a positive integer")
    exit()
else:
    print(f"The integers that are factors of {positive_int} are: ")
    #Start at 1 first positive integer
    x = 1
    while x <= positive_int: #iterate to positive_int
        #If integer has no remainder when dividing by num x, x is a factor
        if positive_int%x == 0:
            print(x)
        #Increment up by 1
        x+=1

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]

name = input("Enter your last name: ").lower() #to match alphabet
total = 0
for l in name: #loops through each letter
    position = alphabet.index(l) #returns index of letter in alphabet
    total = total + position #add index to total
print(f"The sum of positions in {name} is {total}")

def recursive(x):
    if x<0:
        print('Enter a positive integer')
        return #stop function for negative integers
    if x == 0:
        return #base case
    recursive(x - 1) #iterate down by 1
    print(x**2) #print squared x

x = int(input("Enter a positive integer: "))
recursive(x) #call function

#Teepee sort
def teepee (x):
    """This function creates
    a sorted list with the largest number in the center
    and odd ascending to left and even descending to right """
    #Find largest number:
    large = max(x)
    #Discovered sorted function, if num divided by 2's remainder is not 0 and num is not large
    odd = sorted([num for num in x if num % 2 != 0 and num != large])
    #Reversed sorted function for even, if num divided by 2's remainder is 0 and num is not large
    even = sorted([num for num in x if num % 2 == 0 and num != large], reverse=True)
#concatenate all together, [large] so the integer beomces a list
    return odd + [large] + even
#split splits string into pieces
#map converts each str into integer
#list stores result as list of integers
x = list(map(int, input("Enter numbers with spaces: ").split()))
print(teepee(x))


#Didn't fully understand this question, spent a lot of time googling
#Not sure about my solution
def find_next(num):
    #converting numbers to list of characters
    nums = list(str(num))

    def check(pos):
        #base case, checking everything & finding nothing
        if pos < 0:
            return None
        #going from right to left
        for p in range(len(nums) - 1, pos, -1):
            #if a bigger number is found than current position
            if nums[p] > nums[pos]:
                # Swapping numbers
                nums[pos], nums[p] = nums[p], nums[pos]
                # Sort remaining numbers
                nums[pos + 1:] = sorted(nums[pos + 1:])
                #convert back from characters to integers
                return int(''.join(nums))

        #this is if no bigger number is found, look left
        return check(pos-1)
    #checking second to last
    return check(len(nums)-2)
#Testing
num = int(input("Enter a integer: "))
print(f"{num} -> {find_next(num)}")