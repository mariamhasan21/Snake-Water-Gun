# Snake-Water-Gun
Program Overview

This is a simple text-based game where the player competes against the computer in a variation of "Water, Snake, Gun" (similar to the classic game "Rock, Paper, Scissors"). The objective of the game is for the player to choose between Water, Snake, or Gun, and then compare their choice against the computer's randomly generated choice. The game determines whether the player wins, loses, or if it’s a draw.


Features:
```
1. Random Computer Choice: The computer randomly selects either "Water", "Snake", or "Gun" for each round.
2. Case-Insensitive Input: Players can type their choices in any combination of uppercase or lowercase letters (e.g., "WATER", "snake", "Gun"). The program will still accept the input as valid.
3. Multiple Rounds: After each round, the player is asked if they want to play again. The game continues until the player chooses to quit.
4. Win, Lose, or Draw Outcome: The game evaluates each round and displays whether the player has won, lost, or tied with the computer.
5. Game Rounds Counter: The program tracks how many rounds have been played and displays the total count at the end of the session.
```

Game Logic:
```
1. Water beats Gun (Water makes the Gun useless).
2. Gun beats Snake (The Gun can shoot the Snake).
3. Snake beats Water (The Snake can survive in Water and defeat it).
4. If both the player and the computer choose the same option, the round results in a draw.
```
Example Playthrough:
```
1. The player is asked to choose between Water, Snake, or Gun.
2. The computer randomly selects its option.
3. The game announces the outcome (Win, Lose, or Draw).
4. The player is asked if they would like to play another round.
5. The game continues until the player decides to quit, and the total number of rounds is displayed.
```
