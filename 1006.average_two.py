"""
Read three values (variables A, B and C),
which are the three student's grades. Then, calculate the average,
considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5.
Consider that each grade can go from 0 to 10.0, always with one decimal place.

Input
The input file contains 3 values of floating points (double) with one digit after the decimal point.

Output
Print the message "MEDIA"(average in Portuguese) and the student's average according to the following example,
with a blank space before and after the equal signal.
"""

""" Solution (A) """
# Read three student grades as floating-point numbers.
# Each input is expected to have one decimal place (e.g., 7.5).
A = float(input())
B = float(input())
C = float(input())

# Compute the weighted average.
# Weights are defined as:
# A → 2, B → 3, C → 5
# Total weight = 10
avg = ( (A * 2) + (B * 3) + (C * 5)  ) / ( 2 + 3 + 5)

# Output the result in the required format:
# - "MEDIA = " followed by the average
# - Rounded to 1 decimal place
print(f"MEDIA = {avg:.1f}")


""" Solution (B) """
# Read three values (variables A, B and C), which are the three student's grades.
# calculate the average of (variables A, B and C)
# grade A has weight 2, grade B has weight 3, grade C has weight 5.
# Print the message "MEDIA" and the student's average
print(f"MEDIA = {( ( float(input()) * 2) + ( float(input()) * 3) + ( float(input()) * 5)  ) / ( 2 + 3 + 5):.1f}")
