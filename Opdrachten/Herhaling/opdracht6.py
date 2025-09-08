# Maak een functie genaamd rekenmachine met 3 argumenten:

#   - getal1
#   - getal2
#   - operatie

# De operatie kan plus, min, keer of delen zijn. 

# Doe iets met getal1 en getal2 afhankelijk van de operatie en return het resultaat.
# Dus als operatie plus is tel je de 2 getallen bij elkaar op, enz.
# Voer hierna de functie uit met verschillende inputs en bekijk de resultaten.
# Let op: Het is verplicht om een functie te gebruiken!

def rekenmachine(getal1, getal2, operatie):
    if operatie == "plus" or operatie == "+":
        print(getal1 + getal2)
    elif operatie == "min" or operatie == "-":
        print(getal1 - getal2)
    elif operatie == "keer" or operatie == "x" or operatie == "*":
        print (getal1 * getal2)
    elif operatie == "delen" or operatie == "/" or operatie == ":" or operatie == "gedeeld door":
        print (getal1 / getal2)
    else: print("error")

rekenmachine(1, 2, "delen")