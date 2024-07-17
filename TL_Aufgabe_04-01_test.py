#  Mitmachübung Funktionen (mit "define")

def variablen_ausgabe(parameter1):
  print("Übergeben wurde der Wert:",parameter1)
  a = 1
  print (a)
def summe(parameter_a,parameter_b):
  summe = parameter_a + parameter_b
  a=50
  print (a)
  return summe

a = 100  
uebergabewert_1 = 5
variablen_ausgabe(uebergabewert_1)

uebergabewert_2 = 6
meine_summe = summe(uebergabewert_1,uebergabewert_2)
variablen_ausgabe(meine_summe)

print (a)