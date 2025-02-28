#CS161 Week 8
import time
import sys
sys.setrecursionlimit(2000)
#to avoid recursion limit


x = (input("Enter a phrase: ")).upper()
y = (input("Enter the phrase in uppercase: "))
if x == y:
    print("STOP SHOUTING PLEASE")

z = input("Enter a string: ").lower()
vowel = 0
if ('a' in z):
    vowel += 1
if ('e' in z):
    vowel += 1
if ('i' in z):
    vowel += 1
if ('o' in z):
    vowel += 1
if ('u' in z):
    vowel += 1
if ('y' in z):
    vowel += 0.5 #sometimes y
print(f"{z} has {vowel} vowels") #print results

t = input("Enter a string: ").lower() #lower to ensure case sensitivity is not a problem
v = input("Enter another string: ").lower()
if t < v:
    print(f"{t} comes before {v}") #print results
else: print(f"{v} comes before {t}")

while True:
    email = input("Enter your email address: ").lower()
    email1 = input("Verify your email again: ").lower()
    if email == email1: #easier than !=
        print("Thank you!")
        break

    else: print("The two inputs did not match, try again.")

#Iterative function first

def iterative(x):
    r = 1
    while x > 1:
        r *= x #multiply and assign - r = r * x
        x -= 1 # x = x - 1
    return r

def recursive(x):
    return 1 if x == 1 else x * recursive(x - 1)

num_list = [3, 10, 25, 1000]  # Test values

for num in num_list:
    start = time.perf_counter_ns()
    iterative(num)
    iterative_time = time.perf_counter_ns() - start

    start = time.perf_counter_ns()
    recursive(num)
    recursive_time = time.perf_counter_ns() - start

    print(f"{num} - Iterative: {iterative_time}ns | Recursive: {recursive_time}ns")
#recursion wins in very small and very large cases
