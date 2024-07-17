# Kapitel 4 Chalange 1 
# Funktion ohne Rückgabe zur Ausgabe einer Liste

def ausgabe_meine_liste (liste):
  print("Das ist der Inhalt der Liste:")

  for list_content in liste:
    print(list_content)

meine_liste = [0, 2, 4, 8, 16]
ausgabe_meine_liste (meine_liste)