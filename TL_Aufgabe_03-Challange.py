# Lösung von Torsten zu Challange Kapitel 3

meine_liste = [0,0,0,0,0]

# weise jedem Wert im Array den 3fachen Wert des Index zu
for i in range(5):
  meine_liste[i] = i*3

meine_liste_anzahl_groessergleich6 = 0

# gebe die Anzahl der Werte aus, die größer gleich 6 sind
for i in range(5):
  if meine_liste[i] >=6:
    meine_liste_anzahl_groessergleich6 = meine_liste_anzahl_groessergleich6 + 1
  
print('Liste "meine_liste: ', meine_liste)
print('Die Anzahl der Werte größer, gleich 6 in der Lieste "meine_liste" ist: ', meine_liste_anzahl_groessergleich6)

# gebe alle Werte der Liste aus, die größer gleich 6 sind

# for i in range(5):
#  if meine_liste[i] >= 6:
#    print('Dieser Wert der Liste "meine_liste" ist größer gleich 6: ', meine_liste[i])
for value in meine_liste:
  if value >=6:
    print('Dieser Wert der Liste "meine_liste" ist größer gleich 6: ', value)
