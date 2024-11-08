#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. 
    Write a program that solves the N queens problem.

    Usage: nqueens N
    If the user called the program with the wrong number of arguments, print Usage: nqueens N, 
    followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
"""

import sys

def solve_nqueens(N):
    """This Return a solved value of N Queens"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = []
    board = [-1] * N
    cols = set()
    diag1 = set()
    diag2 = set()
    
    def track_row(row):
        """Return a backrack of each Rows"""
        if row == N:
            # A solution is found, record it
            solution = [[r, board[r]] for r in range(N)]
            solutions.append(solution)
            return
        
        for col in range(N):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  

            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            track_row(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board[row] = -1
    
    track_row(0)
    
    for solution in solutions:
        print(solution)

def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_nqueens(N)

if __name__ == "__main__":
    main()