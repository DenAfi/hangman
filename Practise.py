import random
def h(word):
    wrong=0
    stages = ["",
              "_______      ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|    / | \   ",
              "|     / \    ",
              "|            ",
              ]
    rletters = list(word)
    board=list()
    for i in range (len(word)):
       board.append("_")
    win = False
    print("Добро пожаловать на казнь!")
    while wrong<len(stages)-1:
        print("\n")
        msg = "Ввелите букву: "
        char = input(msg)
        if char in rletters:
            coun = rletters.index(char)
            board[coun] = char
            rletters[coun] = "$"
        else:
            wrong+=1
        print((" ".join(board)))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы победили! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Ві проиграли! Было загадано слово:{}.".format(word))

word = ("cat", "dog", "ship", "sheep", "drug", "honor")

h(word[random.randint(0,5)])
        
