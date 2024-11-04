##############################################
# Program: Recursive Addition of Two Numbers
# Author: Sarju S
# Date: 23-10-2024
# Description: This program defines a recursive function to add two positive
#              numbers. The function repeatedly adds 1 to the first number
#              and decreases the second number by 1 until the second number
#              becomes zero.
# Inputs: Two positive integers from the user.
# Outputs: The sum of the two numbers.
##############################################

# Recursive function to add two numbers
def add(a, b):
    # Base case: when one of the numbers becomes 0
    if b == 0:
        return a
    else:
        # Recursion: add 1 to 'a' and decrease 'b' by 1
        return add(a + 1, b - 1)

# Input two positive numbers
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

# Ensure both inputs are positive
if num1 >= 0 and num2 >= 0:
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")
else:
    print("Please enter positive numbers only.")
