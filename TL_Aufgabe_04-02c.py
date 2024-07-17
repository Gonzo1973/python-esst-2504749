# Kapitel 4 Chalange 3
# Funktion mit Rückgabewert bool

def variablenvergleich (par_01, par_02, par_03):
  if (par_01 < par_02) and (par_02 < par_03):
    return True
  else:
    return False
  
variable_1 = 2
variable_2 = 3
variable_3 = 6

ergebnis_vergleich = variablenvergleich(variable_1,variable_2,variable_3)
if ergebnis_vergleich == True:
  ergebnis_vergleich = "korrekt"
else:
  ergebnis_vergleich = "falsch"
print("Die Aussage ist", ergebnis_vergleich, "." )
