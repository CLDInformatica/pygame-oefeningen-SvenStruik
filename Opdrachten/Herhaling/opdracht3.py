'''
Gegeven is een lijst met games. Doe het volgende:

  - Voeg Super Mario Bros toe aan de lijst
  - Vraag de gebruiker om een **getal** tussen de 0 en de 5
  - Print de game die op deze plek in de lijst staat
  - Vraag de gebruiker om een game met een input
  - Voeg deze game toe aan de lijst
  - Print de lijst met games
'''

games = ["Minecraft", "Rust", "GTA V", "Hayday", "Clash of clans"]
games.append("Super Mario Bros")
game = int(input("Geef een getal van 0 tot 5"))
print(games[game])
nogeengame = input("Voeg een game toe")
games.append(nogeengame)
print(games)