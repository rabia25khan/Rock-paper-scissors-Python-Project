def get_choice(player):
    choice = input(f"{player}, enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print(" Invalid choice! Try again.")
        choice = input(f"{player}, enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return " It's a tie!"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return " Player 1 wins!"
    else:
        return " Player 2 wins!"

print(" Rock, Paper, Scissors - Two Players Mode ")
player1_choice = get_choice("Player 1")
player2_choice = get_choice("Player 2")

print("\n Results:")
print(f"Player 1 chose: {player1_choice}")
print(f"Player 2 chose: {player2_choice}")
print(determine_winner(player1_choice, player2_choice))
