import random

guess = 0
tries = 0
number = random.randint(1,10)

name = input("Howdy, May I Know Your Name ")
print("Hello "+name+".")

question = input("Are you ready to guess? [Y/N] ")

if question.lower() == 'n':
    print("Ohh, then we meet next time...")
    exit()
if question.lower() == 'y':
    print("I'm thinking of a number between 1 & 10")    


while not(guess == number):
    guess = int(input("What's your guess? "))
    tries = tries + 1
    if guess == number:
        print("Brilliant")
        print("Congrats, Your guess was correct. The number was indeed {}.".format(number))
        print("It has taken you {} tries".format(tries))
    elif guess < number:
        print("No! Guess Higher")
    elif guess > number:
        print("No! Guess Lower")        

