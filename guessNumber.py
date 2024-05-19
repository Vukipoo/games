import random  
import time                          

guessesTaken = 0                     

print("hello what is ur name")
myName = input()
number = random.randint(1, 2)
print("hello " + myName + " i am thinking of a number between 1 anfd 2")
time.sleep(1)

for guessesTaken in range(6):
    print("take a guess")
    guess = int(input())

    if guess < number:
        print('too low, again')

    if guess > number:
        print('too high, go again')

    if guess == number:
        break

if guess == number:
    guessesTaken += 1
    if guessesTaken == 1:
        print("u actually got it on the first try, good stuff")
    else:
        print("it only took you " + str(guessesTaken) + " times to get it, good job though")

if guess != number:
    print('nope, the number i was thinking of is ' + str(number))
