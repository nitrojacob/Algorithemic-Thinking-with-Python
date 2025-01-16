'''
Description: program to play a sticks game in which there are 16 sticks. Two players take turns to play the
game. Each player picks one set of sticks (needn’t be adjacent) during his turn. A set contains 1, 2,
or 3 sticks. The player who takes the last stick is the loser. The number of sticks in the set is to be
input.
Author: Sarju S
Date: November  13  2024
Version: 1.0
'''

def sticks_game():
    total_sticks = 16
    print("Welcome to the Sticks Game!")
    print("Rules: You can pick 1, 2, or 3 sticks in one turn.")
    print("The player who picks the last stick loses.")

    # Player names
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")

    current_player = player1

    while total_sticks > 0:
        print(f"\nSticks remaining: {total_sticks}")
        # Input number of sticks the current player wants to pick
        sticks_picked = int(input(f"{current_player}, pick 1, 2, or 3 sticks: "))

        # Validate the input
        if sticks_picked < 1 or sticks_picked > 3:
            print("Invalid choice! You can only pick 1, 2, or 3 sticks.")
            continue
        if sticks_picked > total_sticks:
            print(f"You can't pick more sticks than are remaining! ({total_sticks} left)")
            continue

            # Update the total number of sticks
        total_sticks -= sticks_picked

            # Check if the game is over
        if total_sticks == 0:
            print(f"\n{current_player} picks the last stick and loses the game!")
            break

            # Switch to the other player
        current_player = player2 if current_player == player1 else player1




# Run the game
sticks_game()
