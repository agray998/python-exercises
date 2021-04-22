win = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
player_1 = str(input("What is player one's name? "))
player_2 = str(input("What is player two's name? "))
player_1_choice = str(input("Player 1: Rock, paper or scissors? "))
player_2_choice = str(input("Player 2: Rock, paper or scissors? "))
if win[player_1_choice] == player_2_choice:
    print(f"{player_2} wins")
else:
    print(f"{player_1} wins")
