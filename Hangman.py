import random
import os

def run():
    words = [
        "HOLA",
        "EQUISDE",
        "ARROZ CON POLLO",
        "MANCHESTER UNITED",
        "VISUAL STUDIO CODE",
        "ARBOL",
        "CRISTIANO RONALDO",
        "RIKO LA ROBA AMIGAS",
        "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
        "DESOXIRRIBONUCLEICO",
        "ESTRERNOCLEIDOMASTOIDEO",
        "AUDIFONOS",
        "MIA TAYLOR",
        "GOOOOOOOOOOOOGLE",
        "PARC DES PRINCES"
    ]

    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
         |
         |
    =========''', '''
    +---+
    |   |
    O  |
   /|   |
         |
         |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
          |
          |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /     |
          |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
          |
    =========''']

    word = random.choice(words)
    spaces = ["_"] * len(word)
    attempts = 0

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(HANGMANPICS[attempts])
        letter = input("Ingresa una letra: ").upper()

        found = False
        for i, character in enumerate(word):
            if character == letter:
                spaces[i] = letter
                found = True

        if not found:
            attempts += 1

        if "_" not in spaces:
            os.system("cls")
            print("Ganaste")
            break

        if attempts == 6:
            os.system("cls")
            print("Perdiste")
            break

if __name__ == "__main__":
    run()