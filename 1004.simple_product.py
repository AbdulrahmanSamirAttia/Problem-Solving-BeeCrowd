"""
Read two integer values.
After this,
calculate the product between them and store the result in a variable named PROD.
Print the result like the example below.
Do not forget to print the end of line after the result, otherwise you will receive “Presentation Error”.

Input
The input file contains 2 integer numbers.

Output
Print the message "PROD" and PROD according to the following example, with a blank space before and after the equal signal.
"""


""" Solution (A) """
# Input: Read Two Integer Variables
A = int(input())
B = int(input())

# Process: Calculate prod of A and B, Then assign it to the variable PROD
PROD = A * B

# Output: Print the message "PROD" with all the capital letters,
print(f"PROD = {PROD}")


""" Solution (B) """
# Printing the message "PROD" with prod of Two Numbers,

print(f"PROD = {int(input()) * int(input())}")

