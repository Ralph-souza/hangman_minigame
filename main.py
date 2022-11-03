import random


def get_word():
    with open('Lista-de-Palavras.txt', 'r') as word:
        words = word.readlines()
    while True:
        random_word = random.choice(words).strip()
        if len(random_word) >= 13:
            return random_word


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
        choice = int(input("Select your option: "))
        match choice:
            case 0:
                print("Leaving the game! See you soon.")
            case 1:
                print("Let`s start. Choose your letter to find out the word!")
                break


def hangman():
    menu()
    word = get_word()
    hidden_word = []
    for _ in word:
        hidden_word.append("_")
    tries = 5
    while tries > 0:
        letter = input("Enter a letter: ").upper()
        if letter in word:
            print(f"Correct! The letter {letter} is in the secret word.")
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            print(hidden_word)
            if ''.join(hidden_word) == word:
                print(f"Correct! The word is {word}")
                break
        else:
            tries -= 1
            print(f"Incorrect! You still have {tries} tries.")
            if tries == 0:
                print(f"You loose! The correct word is {word}")
