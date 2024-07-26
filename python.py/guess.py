import random

print("Welcome to my guessing game!!!")
print("I'm thinking of a number between 1 to 20")
number = random.randint(1, 20)

while True:
    user_input = input("Take a guess: " )
    if user_input == number:
        print("Yay! You guessed the number.")