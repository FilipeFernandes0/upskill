'''import random

guess_board = [[" "]*10 for x in range(1,10)]
hidden_board = [[" "]*10 for x in range(1,10)]

letters_to_numbers = {"A":1 ,"B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9}






def print_board(board):

    print("     A B C D E F G H I")
    print("     -----------------")
    row_number = 1
    for row in board:
        print (row_number, " ".join(row))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = random.randint(1,10), random.randint(1,10)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = random.randint(1,10), random.randint(1,10)
        board[ship_row][ship_column] = "X"

def get_ships_location():
    row = input("Enter a row betwen 1-9: ")
    while row not in "123456789":
        print("your number doenst exist")
        row = input("Enter a row betwen 1-9: ")
    column = input("enter a letter betwen A-I: ").upper()
    while column not in "ABCDEFGHI":
        print("you introduce an invalid character")
        column = input("enter a letter betwen A-I: ").upper()
    return int(row)-1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


#print(create_ships(hidden_board))
turns = 10
while turns > 0:
    print("welcome to battleship")
    create_ships(hidden_board)
    print_board(hidden_board)
    print_board(guess_board)
    row, column = get_ships_location()
    if guess_board[row][column] == "-":
        print("you already guesed that")
    elif hidden_board[row][column] == "X":
        print("Congratulations you hit the battleship")
        guess_board[row][column] = "X"
        turns -= 1
    else:
        print("sorry, you missed")
        guess_board[row][column] = "-"
        turns -=1

    if count_hit_ships(guess_board):
        print("congratulations, you have sunk all the battleships")
        break
    print("you have", turns, "turns remaining")

    if turns == 0:
        print("sorry, GAME OVER")
        break'''









