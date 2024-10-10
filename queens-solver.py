#
# 8 QUEENS PROBLEM
# BDMS Consulting LLC - Miguel Bernadez - 10/10/2024
#
# As a programmatic challenge board will be represented by a number
# each position is represented with 2 bits:
#   00 empty square
#   01 square attacked by a Queen
#   10 square with a Queen
#
# UPDATE VERSION 2
#
# Enhancents
# 
# 1. Manual Interaction finishes when no more squares are available and prints out the time used
# 2. User determines datastructure for board representation: Binary Coding or Standard Array
# 3. User choses results are ploted
#

import os
import sys
import random
import time
import matplotlib.pyplot as plt

# this function clears the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# this function returns standard chess notation from row, col
def get_chess_notation(row, col):
    return chr(col + 64) + str(row)

# this function extracts row, col from standard chess notation
def get_row_col(square):
    row = int(square[1])
    col = ord(square[0]) - 64
    return row, col

# This function gets the value of a specific square using standard notation (A1, B2, etc.)
#
# When binary_coding = True
# filter to extract bits corresponding to the sqare is calculated using this logic
# H1 G1 F1 E1 D1 C1 B1 A1 
# 00-00-00-00-00-00-00-11   3 << 0  Check A1
# 00-00-00-00-00-00-11-00   3 << 2  Check B1
# 00-00-00-00-00-11-00-00   3 << 4  Check C1
# 00-00-00-00-11-00-00-00   3 << 6  Check D1
# 
# When binary_coding = False the position is read from the standard array board_list[row -1][col -1]
def get_square(square):
    global board, board_list, binary_coding

    row, col = get_row_col(square)
    if binary_coding:
        filter = 3 << ( ((row - 1) * 8) + (col - 1) ) * 2
        value = ( board & filter ) >> ( ((row - 1) * 8) + (col - 1) ) * 2
    else:
        value = board_list[row - 1][col - 1]

    return value

# This function marks all attacked squares vertically
def set_vertical(square):

    row, col = get_row_col(square)
    for y in range(1, 9):
        if y != row:
            place_attack(get_chess_notation(y, col))
    return

# This function marks all attacked squares horizontally
def set_horizontal(square):

    row, col = get_row_col(square)
    for x in range(1, 9):
        if x != col:
            place_attack(get_chess_notation(row, x))
    return

# This function marks all attacked squares diagonally 
def set_diagonal(square):

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
# 
# If binary_coding = True the filter used to change the corresponding bits is calculated by shifting left the binary value 10 (decimal 2) representing a Queen
def place_queen(square):
    global board, board_list, binary_coding

    value = get_square(square) # Gets de value of the square
    if not value: # If square is empty places the Queen
        row, col = get_row_col(square)
        if binary_coding:
            filter = 2 << ( ((row - 1) * 8) + (col - 1) ) * 2
            board = board ^ filter
        else:
            board_list[row - 1][col - 1] = 2

        set_horizontal(square)
        set_vertical(square)
        set_diagonal(square)
        return True, 0

    return False, value

# This function sets the value of a particular square to 01 (1 decimal) to indicate that is being attacked by a Queen
def place_attack(square):
    global board, board_list, binary_coding

    if not get_square(square):
        row, col = get_row_col(square)
        if binary_coding:
            filter = 1 << ( ((row - 1) * 8) + (col - 1) ) * 2
            board = board ^ filter
        else:
            board_list[row - 1][col -1] = 1

    return

#this function checks for a square that is free from attack and Queen
def get_available():

    for row in range(1,9):
        for col in range(1,9):
            square = get_chess_notation(row, col)
            if get_square(square) == 0:  # returns the first available square on the board
                return square, True

    return "", False

# This function places N Queens on the board insuring they are not attacking each other
def solve_queens(number, algorithm = 0):
    
    if number <= 0:
        return True, number
    else:
        if algorithm == 0:
            square, available = get_available()
            if available:
                place_queen(square)
                return solve_queens(number - 1, 0)
            else:
                return False, number
        elif algorithm == 1:
            _ , available = get_available()
            if not available:
                return False, number
            else:
                row = random.randint(1, 8) # Placement of Queens is random
                col = random.randint(1, 8)
                valid, value = place_queen(get_chess_notation(row, col))
                if valid:
                    return solve_queens(number -1, 1)
                else:
                    return solve_queens(number, 1)
                    
# This function prints the chess board using standard conventions
def print_board():

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

# User input to compare human performance vs. computing algorithms
def interactive_game():
    number = 0
    start_time = time.time()
    while True:
        print_board()
        print(f"The 'board' variable has a current size of {sys.getsizeof(board)} bytes.")
        if number:
            print(f"{number} Queens placed on the board:")
            suffix = "next"
        else:
            suffix = "first"
        _ , available = get_available()
        if not available:
            print("No more board spaces are available. ")
            end_time = time.time()
            execution_time= end_time - start_time
            print(f"Total Execution time: {execution_time:.6f} seconds")                       
            break
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

# Very poor algorithm using a linear method placing Queens based on standard scanning of the board
# Starting from row 1 and column A
def computer_first_available_algorithm():
    valid, pending = solve_queens(number, 0)
    return valid, pending

# Basic solver that uses random placing and iterates as many times as needed in order to solve 'number' Queens on the board
def computer_random_algorithm(number=8):
    global board, board_list

    valid = False
    tries = 0

    while not valid:
        if binary_coding:
            board = 0
        else:
            board_list = [[0 for x in range(8)] for y in range(8)] 
        tries += 1
        valid, pending = solve_queens(number, 1)
    print(f"After {tries} intents...")
    return valid, pending

# Forces n interations to find how many different solutions can be found
def computer_iterative_solver(iterations=1, number=8, plotting=0):
    global board, board_list, binary_coding

    solutions = []
    
    start_time = time.time()
    tries = [0 for x in range(iterations)]
    for iter in range(iterations):
        valid = False
        while not valid:
            if binary_coding:
                board = 0
            else:
                board_list = [[0 for x in range(8)] for y in range(8)]
            tries[iter] += 1
            valid, pending = solve_queens(number, 1)
        if binary_coding:
            if board not in solutions:
                solutions.append(board)
                display_status(plotting, start_time, len(solutions), tries[iter])
        elif board_list not in solutions:
            solutions.append(board_list)
            display_status(plotting, start_time, len(solutions), tries[iter])
        
    end_time = time.time()
    execution_time= end_time - start_time
    print("\n\nHere are the statistics\n")
    print(f"Total Execution time: {execution_time:.6f} seconds")                       
    print(f"Total number of cycles: {iterations * sum(tries)} (iterations x tries)\n") 
    print(f"After {iterations} iterations the computer found {len(solutions)} solutions. ")
    print("Here is the last one...")

    return valid, pending

# if plotting is True no printing is done to avoid having misleading times due to printing
def display_status(plotting, start_time, solutions, tries):
    global iterations_stat, solutions_stat, time_invested

    if not plotting:
        print(f"Solution {solutions} after {tries} intents")
        print_board()
    else:
        iterations_stat.append(tries)
        solutions_stat.append(solutions)
        time_invested.append(time.time() - start_time)

# takes the lists with key metrics and uses mathplotlib to plot performance
def display_plot(binary_coding):
    global iterations_stat, solutions_stat, time_invested

    plt.figure(figsize=(10,6))

    # Plotting iterations vs. time invested
    plt.plot(time_invested, iterations_stat, label='Iterations', marker='o')

    # Plotting solutions found vs. time invested
    plt.plot(time_invested, solutions_stat, label='Solutions Found', marker='x')

    plt.xlabel('Time Invested (seconds)')
    plt.ylabel('Count')

    if binary_coding:
        plt.title('Iterations and Solutions Found vs. Time Invested. Used Binary Coding for Board Representation')
    else:
        plt.title('Iterations and Solutions Found vs. Time Invested. Standard Array for Board Representation')
    
    plt.legend()
    plt.grid(True)
    plt.show()


clear_screen()
while True:
    try:
        binary_coding = True # Default Value
        iterations_stat = []
        solutions_stat = []
        time_invested = []
        board = 0
        board_list = [[0 for x in range(8)] for y in range(8)]

        tries = 0
        game_type = int(input("How do you want to play? (0 = Computer, 1 = Manual, 2 = Exit): "))
        assert game_type < 3
        if game_type == 0:
            number = int(input('How many Queens do you want to place in the board? '))
            method = int(input('What algorithm? 0 for First Available, 1 for Random, 2 for Iterative: '))
            clear_screen()
            assert number > 0 and number < 9
            assert method >= 0 and method <= 2
            if method == 0:
                valid, pending = computer_first_available_algorithm()
            elif method == 1:
                binary_coding = True
                valid, pending = computer_random_algorithm(number)                
            elif method == 2:
                iterations = int(input('How many iterations do you want to compute? '))
                binary_coding = int(input('Choose Data Structure for Board: (1 - Binary Coding, 0 - Standard Array): '))
                plotting = int(input('Do you want to plot performance? (0- No, 1-Yes): '))
                assert binary_coding == 0 or binary_coding == 1
                assert plotting >= 0 and plotting <= 1
                valid, pending = computer_iterative_solver(iterations, number, plotting)
                if plotting:
                    display_plot(binary_coding)
            print_board()
            if valid:
                print(f"The computer placed {number} Queens on the board!")
            else:
                print(f"Only {number - pending} Queens where placed on the board.")

        elif game_type == 1:
            interactive_game()
        elif game_type == 2:
            break
    except AssertionError:
        print('Invalid Entry. Please try again.')
    except:
        print("There has been an Error in the Program. Please try again.")
clear_screen()


