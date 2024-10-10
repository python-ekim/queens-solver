#
# 8 QUEENS PROBLEM
# BDMS Consulting LLC - Miguel Bernadez - 10/10/2024
#
# As a programmatic challenge board will be represented by a number
# each position is represented with 2 bits:
#   00 empty square
#   01 square attacked by a Queen
#   10 squere with a Queen

import os

# this function clears the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# this function returns standard chess notation from row, col
def get_chess_notation(row, col):
    return chr(col + 64) + str(row)

# this function extracts row, col from a square with chess notation
def get_row_col(square):
    row = int(square[1])
    col = ord(square[0]) - 64
    return row, col

# This function gets the value of a specific square using standard notation (A1, B2, etc.)
#
# A8 B8 C8 D8 E8 F8 G8 H8 A7 B7 C7 D7 E7 F7 G7 H7 A6 B6 C6 D6 E6 F6 G6 H6 A5 B5 C5 D5 E5 F5 G5 H5 A4 B4 C4 D4 E4 F4 G4 H4 A3 B3 C3 D3 E3 F3 G3 H3 A2 B2 C2 D2 E2 F2 G2 H2 A1 B1 C1 D1 E1 F1 G1 H1
# 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00
#
# H1 G1 F1 E1 D1 C1 B1 A1 - values from 0 to 65535
# 00-00-00-00-00-00-00-00
#
# check value 0f D1
# H1 G1 F1 E1 D1 C1 B1 A1 
# 00-00-00-00-00-00-00-11   3 << 0  Check A1
# 00-00-00-00-00-00-11-00   3 << 2  Check B1
# 00-00-00-00-00-11-00-00   3 << 4  Check C1
# 00-00-00-00-11-00-00-00   3 << 6  Check D1

def get_square(square):
    global board

    row, col = get_row_col(square)
    filter = 3 << ( ((row - 1) * 8) + (col - 1) ) * 2

    value = ( board & filter ) >> ( ((row - 1) * 8) + (col - 1) ) * 2

    return value

# This function marks all attacked squares vertically
def set_vertical(square):
    global board

    row, col = get_row_col(square)
    for y in range(1, 9):
        if y != row:
            place_attack(get_chess_notation(y, col))
    return

# This function marks all attacked squares horizontally
def set_horizontal(square):
    global board

    row, col = get_row_col(square)
    for x in range(1, 9):
        if x != col:
            place_attack(get_chess_notation(row, x))
    return

# This function marks all attacked squares diagonally 
def set_diagonal(square):
    global board

    row, col = get_row_col(square)
    # places attacks upper left
    x = col - 1
    for y in range(row - 1, 0, -1):
        if x >= 1:
            place_attack(get_chess_notation(y, x))
            x -= 1
    # places atttacks upper right
    x = col + 1
    for y in range(row - 1, 0, -1):
        if x <= 8:
            place_attack(get_chess_notation(y, x))
            x += 1
    # places attacks bottom left
    x = col - 1
    for y in range(row + 1, 9):
        if x >= 1:
            place_attack(get_chess_notation(y, x))
            x -= 1
    # places attacks bottom right
    x = col + 1
    for y in range(row + 1, 9):
        if x <= 8:
            place_attack(get_chess_notation(y, x))
            x += 1

    return

# This function places a Queen on a specific square using standard notation (A1, B2, etc.)
def place_queen(square):
    global board

    value = get_square(square)
    if not value:
        row, col = get_row_col(square)
        filter = 2 << ( ((row - 1) * 8) + (col - 1) ) * 2
        board = board ^ filter

        set_horizontal(square)
        set_vertical(square)
        set_diagonal(square)
        return True, 0

    return False, value

def place_attack(square):
    global board

    if not get_square(square):
        row, col = get_row_col(square)
        filter = 1 << ( ((row - 1) * 8) + (col - 1) ) * 2
        board = board ^ filter

    return


#this function checks for a square that is free from attack
def get_available():
    global board
    
    for row in range(1,9):
        for col in range(1,9):
            square = get_chess_notation(row, col)
            if not get_square(square):
                return square, True

    return "", False

# This function places N Queens on the board insuring they are not attacking each other
def solve_queens(number):
    global board
    if number <= 0:
        return True, number
    else:
        square, available = get_available()
        if available:
            place_queen(square)
            return solve_queens(number - 1)
        else:
            return False, number


# This function prints the chess board using standard conventions
def print_board():
    global board

    print("    A     B     C     D     E     F     G     H ")
    print("  _____ _____ _____ _____ _____ _____ _____ _____")
    for row in range(8,0,-1):
        print(" |     |     |     |     |     |     |     |")
        print(row, end="")
        for col in range(1,9):
            value = get_square(get_chess_notation(row, col))
            if  value == 1:
                print("|  .  ", end="")
            elif value == 2:
                print("|  Q  ", end="")
            elif not value:
                print("|     ", end="")
        print(f" {row}")
        print(f" |     |     |     |     |     |     |     | ")
        print("  ----- ----- ----- ----- ----- ----- ----- -----")
    print("    A     B     C     D     E     F     G     H  ")
    return

clear_screen()
while True:
    try:
        board = 0
        game_type = int(input("How do you want to play? (0 = Computer, 1 = Manual, 2 = Exit): "))
        assert game_type < 3
        if game_type == 0:
            number = int(input('How many Queens do you want to place in the board? '))
            clear_screen()
            assert number > 0 and number < 9
            valid, pending = solve_queens(number)
            print_board()
            if valid:
                print(f"The computer placed {number} Queens on the board!")
            else:
                print(f"Only {number - pending} Queens where placed on the board.")
        elif game_type == 1:
            number = 0
            while True:
                print_board()
                if number:
                    print(f"{number} Queens placed on the board:")
                    suffix = "next"
                else:
                    suffix = "first"
                print(f"Where do you want to place your {suffix} Queen? (A1, B4, H8, Enter for exit): ", end="")
                square = input().upper()
                clear_screen()
                if square == "":
                    break
                valid, value = place_queen(square)
                if valid:
                    number += 1
                elif value == 1:
                    print("That square is being attacked. ")
                elif value == 2:
                    print("You have already placed a Queen in that square. ")
        elif game_type == 2:
            break
    except AssertionError:
        print('Invalid Entry. Please try again.')
    except:
        print("Check your Entry. Please try again.")


