#Snake Water Gun
import random
options = ("water", "snake", "gun")
running = True
times = 0
while running:
    user = None
    computer = random.choice(options)
    while user not in [option.lower() for option in options]: #this converts the tuple to a list to compare the tuple items in lowercase
        user = input("Pick one\nWater, Gun, Snake: ").lower()
        times += 1


    print(f"Player = {user.capitalize()}")
    print(f"Computer = {computer.capitalize()}")

    #game conditions starts from here
    if user == computer:
        print("It's a draw!")
    elif user == "water" and computer == "gun":
        print("You win!")
    elif user == "gun" and computer == "snake":
        print("You win!")
    elif user == "snake" and computer == "water":
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
        break

print(f"Thanks for playing! The number you played the game {times} times")
