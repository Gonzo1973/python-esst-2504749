# Challange 06 - Tic Tac Toe - Revision 2
"""
Changes to Rev1:
- playing in blank playing field for better visibility of player's choises
- Function checkWinner:
  not checking for the equal fields but for equal to player ('x' or 'o') 
  Thus, with second parameter to use player ('x' or 'o') 


  Open for Rev4:
  - optimize code
  
  - check for wrong input by player
"""

import os

# Function to show play field
def show_playField(playField):
  # Clearing the Screen
  os.system('cls')

  # Display playing field
  print("\n ", playField[0]," | ", playField[1]," | ", playField[2])
  print("-----------------")
  print(" ", playField[3]," | ", playField[4]," | ", playField[5])
  print("-----------------")
  print(" ", playField[6]," | ", playField[7]," | ", playField[8])


# Check if current player is the winner
def checkWinner(playField, player):
  if playField[0] == player and playField[1] == player and playField[2] == player:
    return True
  elif playField[3] == player and playField[4] == player and playField[5] == player:
    return True
  elif playField[6] == player and playField[7] == player and playField[8] == player:
    return True
  elif playField[0] == player and playField[3] == player and playField[6] == player:
    return True
  elif playField[1] == player and playField[4] == player and playField[7] == player:
    return True
  elif playField[2] == player and playField[5] == player and playField[8] == player:
    return True
  elif playField[0] == player and playField[4] == player and playField[8] == player:
    return True
  elif playField[2] == player and playField[4] == player and playField[6] == player:
    return True
  else:
    return False

# Introduction of playing field to the players
playField = ["1","2","3","4","5","6","7","8","9"]
show_playField(playField)
print("\nWelcome to our Tic Tac Toe Game! :-)")
print("This is your playing field.\n")
print("\nPlease use the numbers 1 to 9 to indicate your chosen field.")
input("Press ENTER when your are ready.")

# Clearing the playing field and initializing variables
playField = [" "," "," "," "," "," "," "," "," "]
show_playField(playField)

winner = False
unentschieden = False

# main
while True:
  # player x's turn
  player = "x"
  player_input = int(input("\nPlayer x: make your choise (empty field 1 to 9): "))
  playField [player_input - 1] = player
  winner = checkWinner(playField, player)
  show_playField(playField)
  
  if not " " in playField:
    unentschieden = True
    break
    
  if winner:
    break 

  # player o's turn
  player = "o"
  player_input = int(input("\nPlayer o: make your choise (empty field 1 to 9): "))
  playField [player_input - 1] = player
  winner = checkWinner(playField, player)
  show_playField(playField)
  
  if not " " in playField:
    unentschieden = True
    break
    
  if winner:
    break 
  
if winner:
  print("\nThe Winner is player ",player," !")

if unentschieden:
  print("\nNo loser and no winner :-) !")


