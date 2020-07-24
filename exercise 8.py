#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules: Rock beats scissors / Scissors beats paper / Paper beats rock

















player1 = input("Rock, Paper, Scissors?: ")
player2 = input("Rock, Paper, Scissors?: ")

if player1.lower() == player2.lower():
    print("tie")
elif player1.lower() == "rock":
    if player2.lower() == "paper":
        print("Paper wins")
    elif player2.lower() == "scissors":
        print("Rock wins")
elif player1.lower() == "paper":
    if player2.lower() == "rock":
        print("Rock wins")
    elif player2.lower() == "scossors":
        print("Scossors wins")
elif player1.lower() == "scossors":
    if player2.lower() == "rock":
        print("Rock wins")
    elif player2.lower() == "paper":
        print("Scossors wins")
else:
    print("invalid input")

