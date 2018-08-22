### HANGMAN GAME ###

def hangman(word):
    wrong_guess = 0
    # Total 8 stages; 0 to 7 
    stages = ["",                   # 0
             "________        ",    # 1
             "|               ",    # 2
             "|        |      ",    # 3
             "|        0      ",    # 4
             "|       /|\     ",    # 5
             "|       / \     ",    # 6
             "|               "     # 7
              ]
    letter = list(word)
    board = ["_"] * len(word) # Store guessed letters
    win = False
    print("Welcome to Hangman")
    print("\nBoard: ")
    print(" ".join(board))
    
    while wrong_guess < len(stages) - 1: # begin with "0"
        print("\n")
        g_letter = input("Guess a letter: ")
        
        if g_letter in letter:
            letter_i = letter.index(g_letter)
            board[letter_i] = g_letter
            letter[letter_i] = 'done' # mark correctly guessed letter as done, in case a word that has duplicate letters
            print("That's right :D\n")
        else:
            wrong_guess += 1
            print("Wrong!\n")
            
        print(" ".join(board))
        current_stage = wrong_guess + 1
        print("\n".join(stages[0:current_stage])) # end_index = index + 1
    
        if "_" not in board:
            print("\nYou win!\n")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[:]))
        print("\nYou lose! It was '{}'.".format(word))

hangman("shazarm")
