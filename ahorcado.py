#!/usr/bin/env python3


import random

HANGMAN_PICS = [
    "\n\n\n\n\n\n",
    "\n\n\n\n\n___\n",
    " |\n |\n |\n |\n |\n_|_\n",
    " ____\n |   |\n |\n |\n |\n_|_\n",
    " ____\n |   |\n |   O\n |\n |\n_|_\n",
    " ____\n |   |\n |   O\n |  /|\\\n |\n_|_\n",
    " ____\n |   |\n |   O\n |  /|\\\n |  / \\\n_|_\n",
]

WORDS = [
    "gato",
    "perro",
    "casa",
    "arbol",
    "libro",
    "python",
    "sol",
    "luna",
]

MAX_WRONG = len(HANGMAN_PICS) - 1


def display_state(word, guessed_letters, wrong):
    print(HANGMAN_PICS[wrong])
    shown = " ".join([c if c in guessed_letters else "_" for c in word])
    print("Palabra: ", shown)
    print("Letras usadas:", " ".join(sorted(guessed_letters)))
    print(f"Intentos restantes: {MAX_WRONG - wrong}\n")


def jugar():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("--- Ahorcado (versión corta) ---")
    print("Adivina la palabra. Puedes introducir una letra o intentar la palabra completa.")

    while True:
        display_state(word, guessed, wrong)

        if all(c in guessed for c in word):
            print("¡Felicidades! Has adivinado la palabra:", word)
            break

        if wrong >= MAX_WRONG:
            print("Has perdido. La palabra era:", word)
            break

        intento = input("Introduce letra o palabra: ").lower().strip()
        if not intento:
            continue

        if len(intento) == 1:
            if intento in guessed:
                print("Ya usaste esa letra.")
            elif intento in word:
                guessed.add(intento)
                print("¡Bien! Letra correcta.")
            else:
                guessed.add(intento)
                wrong += 1
                print("Letra incorrecta.")
        else:
            if intento == word:
                print("¡Felicidades! Has adivinado la palabra completa:", word)
                break
            else:
                wrong += 1
                print("Palabra incorrecta.")


if __name__ == "__main__":
    jugar()

