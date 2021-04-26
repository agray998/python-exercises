from numpy import random as rand

win = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'} # Defining combinations of moves as losing move:winning move
mode = str(input("Single player or two player? ")) # User select whether two players or one player vs computer

# Single player mode
if mode == "single player":
    player_1 = str(input("What is your name? ")) # Player inputs name
    player_1_choice = str(input("Rock, paper or scissors? ")) # player chooses move
    if player_1_choice not in win: # Check for validity of move
        print("Invalid move!")
    else:
        pass

    comp_dict = {0: 'rock', 1: 'paper', 2: 'scissors'} # Mapping randints to moves
    comp_choice = comp_dict[rand.randint(2)] computer makes move
    print(f"{player_1} played {player_1_choice}") # print out record of moves
    print(f"computer played {comp_choice}")

# Determining winner
    if player_1_choice == comp_choice:
        print("Draw!")
    elif win[player_1_choice] == comp_choice:
        print("Computer wins")
    else:
        print(f"{player_1} wins")

# Two player mode
elif mode == "two player":
    #Players enter names
    player_1 = str(input("What is player one's name? "))
    player_2 = str(input("What is player two's name? "))
    # Players choose moves
    player_1_choice = str(input("Player 1: Rock, paper or scissors? "))
    player_2_choice = str(input("Player 2: Rock, paper or scissors? "))
    if player_1_choice not in win or player_2_choice not in win:
        print("Invalid move!") # Check for validity of moves
    else:
        pass
    # Print record of moves
    print(f"{player_1} played {player_1_choice}")
    print(f"{player_2} played {player_2_choice}")

# Determining winner
    if player_1_choice == player_2_choice:
        print("Draw!")
    elif win[player_1_choice] == player_2_choice:
        print(f"{player_2} wins")
    else:
        print(f"{player_1} wins")
