"""
Read three integers and sort them in ascending order. After, print these values in ascending order,
a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.


Input Sample	Output Sample
7 21 -14        -14
                7
                21

                7
                21
                -14

-14 21 7        -14
                7
                21

                -14
                21
                7
"""
""" Solution (A) """
a, b, c = map(int, input().strip().split())
o_A, o_B , o_C = a, b, c

tmp = None

# b is the largest
if b > a and b > c:
    tmp = a
    a = b
    b = tmp
    if c > b:
        tmp = b
        b = c
        c = tmp

# c is the largest
elif c > a and c > b:
    tmp = a
    a = c
    c = tmp
    if c > b:
        tmp = b
        b = c
        c = tmp

# a is the largest (already in place), just order b and c
else:
    if c > b:
        tmp = b
        b = c
        c = tmp

print(f"{c}\n{b}\n{a}\n")

print(f"{o_A}\n{o_B}\n{o_C}")


""" Solution (B) """
# # Step 1: Read the three integers
# a, b, c = map(int, input().strip().split())
#
# # Step 2: Save the original values BEFORE sorting
# # This is crucial because the problem requires printing the original order on the second half
# original_a, original_b, original_c = a, b, c
#
# # Step 3: Sort them in ascending order using pairwise swaps
# # We want to ensure a <= b <= c
#
# # If a is bigger than b, swap them → now a is the smaller of the first two
# if a > b:
#     a, b = b, a
#
# # If a is bigger than c, swap them → now a is the smallest of all three
# if a > c:
#     a, c = c, a
#
# # If b is bigger than c, swap them → now b is the middle, c is the largest
# if b > c:
#     b, c = c, b
#
# # Step 4: Output
# # Print sorted values in ascending order (a <= b <= c)
# print(a)
# print(b)
# print(c)
#
# # Print a blank line as required
# print()
#
# # Print the original values as they were read
# print(original_a)
# print(original_b)
# print(original_c)
