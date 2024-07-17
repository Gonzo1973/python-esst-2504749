# Kapitel 4 Chalange 2 
# Funktion mit Rückgabewert

def rechenoperation (var_float_1, var_float_2):
  return (var_float_1*(var_float_2 + 2))

variable_1 = 2.0
variable_2 = 3.0

ergebnis = rechenoperation(variable_1,variable_2)
print("Das ist das Ergebnis aus", variable_1, "* (",variable_2, "+ 2) =", ergebnis)
