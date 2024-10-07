#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal = []

    if n <= 0:
        return pascal
    
    for i in range(n):
        
        row = [1 if j == 0 or j == i else pascal[i-1][j-1] + pascal[i-1][j] for j in range(i + 1)]
        
        pascal.append(row)  
    
    return pascal

