from random import randint



random_number = randint(0,10)

# x = input("Enter any number : ")
# x = int(x)
x = -1



while x != random_number:
    x = input("Enter any number : ")
    x = int(x)
    print("wrong guess")
# if x == random_number:
print("You guessed correctly")
