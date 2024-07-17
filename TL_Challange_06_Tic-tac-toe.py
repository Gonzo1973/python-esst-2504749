# Challange 06 - Tic Tac Toe

# Function to show play field
def show_playField(playField):
  print(playField[0]," | ", playField[1]," | ", playField[2])
  print("-------------")
  print(playField[3]," | ", playField[4]," | ", playField[5])
  print("-------------")
  print(playField[6]," | ", playField[7]," | ", playField[8])

# Function to check on winning-condition
def checkWinner(playField):
  if playField[0] == playField[1] and playField[1] == playField[2]:
    return playField[0]
  elif playField[3] == playField[4] and playField[4] == playField[5]:
    return playField[3]
  elif playField[6] == playField[7] and playField[7] == playField[8]:
    return playField[6]
  elif playField[0] == playField[4] and playField[4] == playField[8]:
    return playField[0]
  elif playField[2] == playField[4] and playField[4] == playField[6]:
    return playField[2]
  elif playField[0] == playField[3] and playField[3] == playField[6]:
    return playField[0]
  elif playField[1] == playField[4] and playField[4] == playField[7]:
    return playField[1]
  elif playField[2] == playField[5] and playField[5] == playField[8]:
    return playField[2]
  else:
    return False

# Initialization of playfield and players
playField = ["1","2","3","4","5","6","7","8","9",]
winner = False

print("Welcome to our Tic Tac Toe Game! :-)")
print("This is our playing field:\n")
show_playField(playField)

while True:
  player_input = int(input("\nPlayer x: make your choise (empty field 1 to 9): "))
  player_input_index = player_input - 1
  playField [player_input_index] = "x"
  winner = checkWinner(playField)
  if winner != False:
    break 
  show_playField(playField)

  player_input = int(input("\nPlayer o: make your choise (empty field 1 to 9): "))
  player_input_index = player_input - 1
  playField [player_input_index] = "o"
  winner = checkWinner(playField)
  if winner != False:
    break 
  show_playField(playField)

print("\nThe Winner is player ",winner," !")
