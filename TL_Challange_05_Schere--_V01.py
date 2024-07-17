# Challange to chapter 5 - Schere, Stein, Papier

import random

# Computer and User choose:
user_input = input("Wähle: Schere, Stein oder Papier: ")

computer_random = random.randint(0,2)
possibleValues = ['Schere', 'Stein', 'Papier']
computer_input = possibleValues[computer_random]

# console output that has been chosen
print("\nDer Spieler hat ", user_input, " ausgewählt.")
print("Der Computer hat ", computer_input, " ausgewählt.")

# Ergebnisermittlung
if user_input == computer_input:
  winner = 'keiner'
elif user_input == 'Schere' and computer_input == 'Stein':
  winner = 'Computer (Stein macht Schere stumpf)'
elif user_input == 'Schere' and computer_input == 'Papier':
  winner = 'Spieler (Schere schneidet Papier)'
elif user_input == 'Stein' and computer_input == 'Papier':
  winner = 'Computer (Papier umwickelt Stein)'
elif user_input == 'Stein' and computer_input == 'Schere':
  winner = 'Spieler (Stein macht Schere stumpf)'
elif user_input == 'Papier' and computer_input == 'Schere':
  winner = 'Computer (Schere schneidet Papier)'
elif user_input == 'Papier' and computer_input == 'Stein':
  winner = 'Spieler  (Papier umwickelt Stein)'

print("\nEs gewinnt: ", winner)