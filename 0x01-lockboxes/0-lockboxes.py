#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """This function determine if locked boxes can be unlocke"""

    n = len(boxes)
    
    
    unlocked = set([0])  
    
    stack = [0]  
    
    while stack:
        
        current_box = stack.pop()
        
        
        for key in boxes[current_box]:
            
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)
    
    if len(unlocked) == n:
        return True
    else:
        return False
