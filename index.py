# -------------- import a random module for computer to choose
import random

# -------------- create a random choice between rock, scissors and paper
while True:
    choices = ["rock", "scissors", "paper"]

    computer = random.choice(choices)
    player = None


#---------- starts all over if the player's choice isn't in choices   
    
    while player not in choices:
# -------------- capture the players input
        player = input(f"rock, scissors or paper \n").lower()
            
        if player not in choices:
            print("Not in choices. Try again")
            
        if player == computer:
            print("Tie")

        elif player == "rock":
            if computer == "scissors":
                print("You win")
            elif computer == "paper":
                print("You lose")

        elif player == "scissors":
            if computer == "rock":
                    print("You lose")
            elif computer == "paper":
                    print("You win")

        elif player == "paper":
            if computer == "rock":
                print("You win")
            elif computer == "scissors":
                  print("You lose")
          
    print("-----------GAME OVER!---------------------")
    print("Do you want to play again? (yes/no)")
#------------ decision to start the game again or not.
    decision = input("> ").lower()
    if decision != "yes":
            break
print("Press the run button to play again")