'''
Description: Suppose you're on a game show, and you are given the choice of three doors: Behind one door is a
car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what is behind the
doors, opens another door, say No. 3, which has a goat. He then asks, "Do you want to pick door No.
2?" Is it to your advantage to switch your choice?
Author: Sarju S
Date: November  13  2024
Version: 1.0
'''
import random

def monty_hall_single_game():
    """
    Simulate a single instance of the Monty Hall game.
    """
    # Randomly place the car behind one of the three doors
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    # Player makes an initial choice
    player_choice = int(input("Choose a door (1, 2, or 3): ")) - 1

    # Host opens a door with a goat (not the player's choice, not the car)
    available_doors = [i for i in range(3) if i != player_choice and doors[i] != 'car']
    host_opens = random.choice(available_doors)

    print(f"The host opens door {host_opens + 1}, revealing a goat.")

    # Ask the player if they want to switch
    switch = input("Do you want to switch your choice? (yes/no): ").strip().lower() == 'yes'

    # If the player switches, choose the remaining unopened door
    if switch:
        player_choice = next(i for i in range(3) if i != player_choice and i != host_opens)

    # Check if the player wins
    if doors[player_choice] == 'car':
        print("Congratulations! You won the car!")
    else:
        print("Sorry, you got a goat.")
    print(f"The car was behind door {doors.index('car') + 1}.")


# Run the game interactively or simulate
print("Welcome to the Monty Hall Game!")
monty_hall_single_game()

