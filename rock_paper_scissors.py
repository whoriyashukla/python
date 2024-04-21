import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_choice = input("Enter rock/paper/scissors or q to quit... ").lower()
    if user_choice == "q":
        break
    if user_choice not in options:
        continue
    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print("The computer picked ", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You win!!!")
        user_wins+=1
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!!!")
        user_wins+=1
        
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!!!")
        user_wins+=1
    else:
        print("You lost!!")    
        computer_wins+=1
        
        
print("You won", user_wins, "times!")
print("Computer won", computer_wins, "times!")
print("Thanks for playing!!!")

# options = ["rock", "paper", "scissors"]
# user_choice = input("Enter rock/paper/scissors or q to quit... ")
# computer_choice = random(options)
# print(computer_choice)


    
    
    