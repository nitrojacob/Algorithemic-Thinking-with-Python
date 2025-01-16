
'''
Description: Input two lists from the user. Merge these lists into a third list such that in the merged list, all even
numbers occur first followed by odd numbers. Both the even numbers and odd numbers should be in
sorted order.
Author: Sarju S
Date: November  13  2024
Version: 1.0
'''
# Step 1: Input two lists from the user
my_list1 = input("Enter numbers for the first list, separated by spaces: ").split()
my_list2 = input("Enter numbers for the second list, separated by spaces: ").split()

# Step 2: Convert each input string in list1 and list2 to an integer
my_list1 = [int(num) for num in my_list1]
my_list2 = [int(num) for num in my_list2]

# Step 3: Merge both lists into a single list
combined_list = my_list1 + my_list2

# Step =4: Separate even and odd numbers
even_numbers = [num for num in combined_list if num % 2 == 0]
odd_numbers =  [num for num in combined_list if num %2 !=0 ]

# Step 5: Sort even and odd numbers
even_numbers.sort()
odd_numbers.sort()

# Step 6: Combine sorted even and odd numbers
merged_list = even_numbers + odd_numbers

# Step 7: Print the result
print("Merged list with even numbers first and odd numbers after, both sorted:", merged_list)
