print("Welcome to the computer game!")

playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Okay! Let's get started!")
    count = 0
    print("First question!")
    x1 = input("What is the capital of India? ")
    if x1.lower() == "new delhi":
        print("Correct answer!!")
        count+=1
    else:
        print("Better luck next time!")
    print("Second question!")
    x2 = input("Which planet is known as the Red Planet? ")
    if x2.lower()  == "mars":
        print("Correct answer!!")
        count+=1
    else:
        print("Better luck next time!")
    print("Third question!")
    x3 = input("What is the largest mammal in the world? ")
    if x3.lower()  == "blue whale":
        print("Correct answer!!")
        count+=1
    else:
        print("Better luck next time!")
    print("Fourth question!")
    x4 = input("How many continents are there in the world? ")
    if x4.lower()  == "7":
        print("Correct answer!!")
        count+=1
    else:
        print("Better luck next time!")
    print("Fifth question!")
    x5 = input("What is the largest ocean on Earth? ")
    if x5.lower()  == "pacific ocean":
        print("Correct answer!!")
        count+=1
    else:
        print("Better luck next time!")
    print("you got", count, "questions right!!!")
    print("Thanks for playing the game!!!")
else:
    print("Thanks for responding!")
    
