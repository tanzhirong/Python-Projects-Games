# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Something was wrong with my input."


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Something was wrong with my input."

    

def rpsls(player_choice): 
    print('\n')
    print("Player chooses "+ player_choice)  
    player_number = name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses "+ comp_choice)
    mod = (player_number - comp_number)%5
    if mod == 0:
        ans = "Player and computer tie!"
    elif mod >= 3:
        ans = "Computer wins!"
    elif mod <= 2:
        ans = "Player wins!"
    print(ans)


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
