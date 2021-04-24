def hangman(word):
    wrong = 0
    stages = ["",
              "___________          ",
              "|                    ",
              "|         |          ",
              "|         O          ",
              "|        /|\         ",
              "|        /\          ",
              "|                    "
        ]
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
       print("\n")
       msg = "Guess a letter"
       char = input(msg)
       if char in remaining_letters:
           cind = remaining_letters.index(char)
           board[cind] = char
           remaining_letters[cind] = '$'
       else:
           wrong += 1
       print(("".join(board)))
       e = wrong+1
       print("\n".join(stages[0:e]))
       if "__" not in board:
           print("You Win!")
           print("".join(board))
           win = True
           break
    if not win:
         print("\n".join(stages[0:wrong]))
         print("You Lose! It was {}.".format(word))
hangman("apple")
    