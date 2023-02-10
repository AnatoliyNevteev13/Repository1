ttt_board = [[" " for _ in range (3)] for _ in range(3)]

def board():
    print("  0 1 2")
    for i, row in enumerate(ttt_board):
        print(i, " ".join(row))

def move(player):
  while True:
     row = input(f"{player}, номер строки:")
     column = input(f"{player}, номер колонны:")
     if row.isdigit() and column.isdigit():
        row, column = int(row), int(column)
        if 0 <= row < 3 and 0 <= column < 3:
           if ttt_board[row][column] == " ":
             ttt_board[row][column] = player
             return
           else:
             print("Клетка занята.")
        else:
             print("За пределами поля.")
     else:
        print("Введите номер корректно.")

def win():
    for row in ttt_board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    for column in range(3):
        if ttt_board[0][column] == ttt_board[1][column] == ttt_board[2][column] and ttt_board[0][column] !=" ":
            return True
        if ttt_board[0][0] == ttt_board[1][1] == ttt_board[2][2] and ttt_board[0][0] != " ":
            return True
        if ttt_board [2][0] == ttt_board [1][1] == ttt_board[0][2] and ttt_board[2][0] != " ":
            return True
        return False

def logic():
    while True:
        board()
        move("X")
        if win():
            print("Выигрывает X")
            break
        board()
        move("0")
        if win():
            print ("Выигрывает 0")
            break
logic()

