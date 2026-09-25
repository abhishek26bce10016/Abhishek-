board = [" " for i in range(9)]

def displayboard():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def checkwinner():
    winningpositions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winningpositions:
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

def checkdraw():
    return " " not in board

player = "X"

print("TIC TAC TOE GAME 🎯")
print("Positions are numbered from 1 to 9")
print()

print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    displayboard()

    print("Player", player, "turn")

    try:
        position = int(input("Enter position (1-9): "))
    except ValueError:
        print("Please enter a number!")
        continue

    if position < 1 or position > 9:
        print("Invalid position!")
        continue

    position = position - 1

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = player

    if checkwinner():
        displayboard()
        print("🎉 Player", player, "wins!")
        break

    if checkdraw():
        displayboard()
        print("Game Draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"