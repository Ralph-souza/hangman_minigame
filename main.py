import os
import random


def get_word():
    with open('Lista-de-Palavras.txt', 'r') as word:
        words = word.readlines()
    random_word = random.choice(words)
    if str(len(random_word) >= 5):
        return random_word.strip()


def show_menu():
    print(f"""
    ***************************
    Welcome to Hangman Minigame
    ***************************
    
    Choose your option:
    
    0 - Exit
    1 - Play game!
    """)


def menu():
    show_menu()
    choice = None
    while choice != 0:
        match choice:
            case 0:
                print("Leaving the game! See you soon.")
            case 1:
                print("Let`s start. Choose your letter to find out the word!")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    cls()


def hangman():
    menu()
    choice = int(input("Select your option: "))

    list = words_list()
    while choice != "0":




    if choice == "0":
        print("Saindo do jogo!")
    else:
        word = list
        hidden_word = " _ " * len(word)
        tries = 5
        guessed = []


