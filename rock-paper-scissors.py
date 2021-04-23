from numpy import random as rand

win = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
mode = str(input("Single player or two player? "))

if mode == "single player":
    player_1 = str(input("What is your name? "))
    player_1_choice = str(input("Rock, paper or scissors? "))
    if player_1_choice not in win:
        print("Invalid move!")
    else:
        pass

    comp_dict = {0: 'rock', 1: 'paper', 2: 'scissors'}
    comp_choice = comp_dict[rand.randint(2)]
    if player_1_choice == comp_choice:
        print(f"{player_1} played {player_1_choice}")
        print(f"computer played {comp_choice}")
        print("Draw!")
    elif win[player_1_choice] == comp_choice:
        print(f"{player_1} played {player_1_choice}")
        print(f"computer played {comp_choice}")
        print("Computer wins")
    else:
        print(f"{player_1} played {player_1_choice}")
        print(f"computer played {comp_choice}")
        print(f"{player_1} wins")

elif mode == "two player":
    player_1 = str(input("What is player one's name? "))
    player_2 = str(input("What is player two's name? "))
    player_1_choice = str(input("Player 1: Rock, paper or scissors? "))
    player_2_choice = str(input("Player 2: Rock, paper or scissors? "))
    if player_1_choice not in win or player_2_choice not in win:
        print("Invalid move!")
    else:
        pass

    if player_1_choice == player_2_choice:
        print(f"{player_1} played {player_1_choice}")
        print(f"{player_2} played {player_2_choice}")
        print("Draw!")
    elif win[player_1_choice] == player_2_choice:
        print(f"{player_1} played {player_1_choice}")
        print(f"{player_2} played {player_2_choice}")
        print(f"{player_2} wins")
    else:
        print(f"{player_1} played {player_1_choice}")
        print(f"{player_2} played {player_2_choice}")
        print(f"{player_1} wins")
