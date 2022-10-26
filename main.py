import random


def words_list():
    with open('Lista-de-Palavras.txt', 'r') as word:
        words = word.read().split()
    random_word = random.choice(words)
    if str(len(random_word) > 5):
        return random_word


def hangman():
    choice = None

    list = words_list()
    while choice != "0":
        print(f"""
        **************************
        Bem vindo ao jogo da Forca
        **************************
        
        Escolha a opcao:
        
        0 - Sair
        1 - Jogar
        """)

    choice = input("Escolha sua opcao: ")

    if choice == "0":
