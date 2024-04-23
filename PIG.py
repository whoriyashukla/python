import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players [2-4]: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players!")
    else:
        print("Invalid, try again!")        

max_scores = 50
player_scores = [0 for _ in range(players)]        

while max(player_scores) < max_scores:
    for players_idx in range(players):
        print("\nPlayer number", players_idx + 1, "turn just started.\n")
        current_scores = 0

        while True:
            should_roll = input("Do you want to roll(y)? ")
            if should_roll != "y":
                break 
            value = roll()
            if value == 1:
                current_scores += 0
                print("You rolled a 1. Your turn is done.")
                break
            else:
                print("You rolled a ", value)
                current_scores+=value

            print("Your score is ", current_scores)  
        player_scores[players_idx] += current_scores
        print("Your total score is:", player_scores[players_idx])  

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)