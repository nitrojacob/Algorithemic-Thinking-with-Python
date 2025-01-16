'''
Objective: Program to construct patterns of stars (*), using a nested for loop.
a)
*
**
***
****
*****
b)
*****
****
***
**
*
c)
    *
   ***
  *****
 *******
*********
d)
*********
 *******
  *****
   ***
    *


Author: Sarju S
Date: 19-11-2024
'''
rows=5
print("Pattern-1")
print("---------")
for i in range(1, rows + 1):  # Outer loop for rows
        for j in range(i):       # Inner loop for stars in each row
            print("*", end="")   # Print star on the same line
        print()
print("Pattern-2")
print("---------")
for i in range(rows, 0, -1):  # Outer loop for rows (decreasing order)
        for j in range(i):        # Inner loop for stars
            print("*", end="")
        print()
print("Pattern-3")
print("---------")
for i in range(1, rows + 1):   # Outer loop for rows
        for j in range(rows - i):  # Inner loop for spaces
            print(" ", end="")
        for k in range(2 * i - 1): # Inner loop for stars
            print("*", end="")
        print()
print("Pattern-4")
print("---------")
for i in range(rows, 0, -1):   # Outer loop for rows (from rows to 1)
        for j in range(rows - i):  # Inner loop for spaces before stars
            print(" ", end="")
        for k in range(2 * i - 1): # Inner loop for stars
            print("*", end="")
        print()
