#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the triangle as an empty list
    pascal = []
    
    # Use a loop to build the triangle row by row
    for i in range(n):
        
        # List comprehension to generate each row
        
        row = [1 if j == 0 or j == i else pascal[i-1][j-1] + pascal[i-1][j] for j in range(i + 1)]
        
        pascal.append(row)  # Append the row to the triangle
    
    return pascal

