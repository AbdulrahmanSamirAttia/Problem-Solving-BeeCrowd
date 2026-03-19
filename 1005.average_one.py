"""
Read two floating points' values of double precision A and B, corresponding to two student's grades.
After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5.
Each grade can be from zero to ten, always with one digit after the decimal point.
Don’t forget to print the end of line after the result, otherwise you will receive “Presentation Error”.
Don’t forget the space before and after the equal sign.

Input
The input file contains 2 floating points' values with one digit after the decimal point.

Output
Print the message "MEDIA"(average in Portuguese) and the student's average according to the following example,
with 5 digits after the decimal point and with a blank space before and after the equal signal.
"""

""" Solution (A) """

# Read two floating-point numbers representing the student's grades
# Each value has one decimal place (as per problem constraints)
A = float(input())
B = float(input())

# Compute the weighted average:
# Grade A has weight 3.5 and grade B has weight 7.5
# Total weight = 3.5 + 7.5 = 11
Avg = ( (A * 3.5) + (B * 7.5) ) / 11

# Output the result in the required format:
# - The label must be "MEDIA"
# - There must be a space before and after '='
# - The average must be displayed with exactly 5 decimal places
print(f"MEDIA = {Avg:.5f}")


""" Solution (B) """

# Read two grades from input, apply weights (3.5 and 7.5),
# compute the weighted average, and print it formatted
# with exactly 5 decimal places as required.
print(f"MEDIA = {( (float(input()) * 3.5) + ( float(input()) * 7.5) ) / 11:.5f}")
