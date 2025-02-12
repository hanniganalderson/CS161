#CS161 Week 6

#Integer input
y = int(input("Enter a number: "))
#Decreasing amount
decrease = int(input("Decrease amount: "))
while y > 0:
    #Divisible by 2, even
    if y % 2 == 0:
        print (f" {y} is even ")
    #Not, odd
    else:
        print (f" {y} is odd")
    y-= decrease
print ('Blastoff!')


#Infinite while loop
while True:
    word = input("Enter a word with over 5 letters: ")
    if len(word) < 5:
        print("goodbye (has 7 letters)")
        break
    print(word, "has", len(word), "letters")

#set word count to 0
word_count = 0

while word_count < 6:
    word = input("Enter a word: ")
    print(word, "has", len(word), "letters")

    if len(word) < 5:
        print("goodbye")
        break
    word_count += 1
if word_count == 6:
    print("loser")

num = 10
while num <= 100:
    print(num, bin(num), hex(num))  #print decimal, binary, and hex
    num += 1  #adding one each time

x = int(input("Enter a number: "))
#Iterative function
def iterative(x):
    while x > 0:
        print('*' * x) #String multiplication!
        x -= 1

#Recursive function
def recursive(x):
    if x == 0: #base case, stop infinite recursion
        return
    print('*' * x)
    recursive(x - 1)
#calling functions
iterative(x)
recursive(x)

def sum_digits(num):
    """
    base case: if num is single digit, return it
    num//10 removes last digit
    num % 10 extracts last digit
    """
    return num if num < 10 \
        else sum_digits(num // 10) + num % 10
#testing
print(sum_digits(11))
print(sum_digits(9999))