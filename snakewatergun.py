#Snake Water Gun
import random
options = ("water", "snake", "gun") #keeping the options in tuple to not alternate them
running = True #running variable was used to loop the program and break if it turns to be false
times = 0 #To count how many times the game was played
while running:
    user = None
    computer = random.choice(options)
    while user not in [option.lower() for option in options]: #this converts the tuple to a new list to compare the items in case sensitive
        user = input("Pick one\nWater, Gun, Snake: ")
        times += 1

    #prints the choosen options
    print(f"Player = {user.capitalize()}")
    print(f"Computer = {computer.capitalize()}")

    #game conditions starts from here
    if user == computer:
        print("It's a draw!")
    elif user == "water" and computer == "gun":
        print("You win!")
    elif user == "gun" and computer == "water":
        print("You lose!")
    elif user == "gun" and computer == "snake":
        print("You win!")
    elif user == "snake" and computer == "gun":
        print("You win!")
    elif user == "snake" and computer == "water":
        print("You lose!")
    elif user == "water" and computer == "snake":
        print("You win!")

    if not input("Play again? (y/n): ").lower() == "y": #if the user do not give input of 'y' the program will stop and show running as false
        running = False 

print(f"Thanks for playing! The number you played the game {times} times")
