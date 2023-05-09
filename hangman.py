def hangman(word):
    score_p1 = 0
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    letters_left = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Bienvenido al Colgado")
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Adivina la letra: ")
        if guess in letters_left:
            while guess in letters_left:
                character_index = letters_left.index(guess)
                letter_board[character_index] = guess
                letters_left[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0:wrong_guesses + 1]))
        if '_' not in letter_board:
            print("Haz ganado la palabra era: {}".format(word))
            win = True
            score_p1 += 50
            print("EL jugador 1 tiene {} puntos".format(score_p1))
            break
    if not win:
        print('\n'.join(stages[0:wrong_guesses]))
        print("Perdiste! La palbra era {}".format(word))


g_word = input("Jugador 1 ingresa la palabra: ")


hangman(g_word)