import random

game_console = """
 _____________________________   
/        _____________        \  
| == .  |             |     o |  
|   _   |             |    B  |  
|  / \  |             | A   O |  
| | O | |             |  O    |  
|  \_/  |             |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           S N K             |  
\_____________________________/"""


# Print the game console
print(game_console)

# Condition for the game
""""
Rock vs. Paper:
--> Paper wins (covers rock).
Rock loses.

Rock vs. Scissors:
Rock wins (crushes scissors).
Scissors lose.

Paper vs. Scissors:
Scissors win (cut paper).
Paper loses.

Same Choices:
If both players choose the same item, it's a tie.
"""


# Taking user input
player_name = input("Enter your name: ")
user_choice = input("Enter your move (Rock, Scissor, Paper): ").capitalize()
computer_choice = random.choice(["Rock", "Paper", "Scissor"])

# Condition for the game:
if user_choice == computer_choice:
    print("Match Tie")
    
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print(f"Paper covers Rock, Computer wins")
    else:
        print(f"Rock smashes Scissors! {player_name} wins")
        
        
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print(f"Scissors cut Paper, Computer wins")
    else:
        print(f"Paper covers Rock! {player_name} wins")
        
        
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print(f"Rock smashes Scissors, Computer wins")
    else:
        print(f"Scissors cut Paper! {player_name} wins")

recently_played_move=print(f"{player_name} has recentenly moved is {user_choice}")