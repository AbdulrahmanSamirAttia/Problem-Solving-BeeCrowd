"""
Read 4 integer values A, B, C and D.
Then if
B is greater than C and #
D is greater than A and
if the sum of C and D is greater than
the sum of A and B and if C and D were positives values and if A is even,

write the message “Valores aceitos” (Accepted values).
Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values.

Input Sample	Output Sample
5 6 7 8         Valores nao aceitos

2 3 2 6         Valores aceitos
"""

""" Solution (A) """
A, B, C, D  = map( int, input().strip().split() )

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


""" Solution (B) """
A, B, C, D  = map( int, input().strip().split() )

# We can make the logic more readable by assigning conditions to variables.
# This makes it clear what each part of the 'if' statement is checking.
sum_cd = C + D
sum_ab = A + B

# Naming the conditions (Boolean variables)
is_b_greater_than_c = B > C
is_d_greater_than_a = D > A
is_sum_cd_greater = sum_cd > sum_ab
are_c_d_positive = C > 0 and D > 0
is_a_even = (A % 2 == 0)

# Now the 'if' statement reads like a sentence:
if (is_b_greater_than_c and
    is_d_greater_than_a and
    is_sum_cd_greater and
    are_c_d_positive and
    is_a_even):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


""" Solution (C) """
A, B, C, D  = map( int, input().strip().split() )

# Nested IF statements.
# This style is helpful if you wanted to tell the user EXACTLY why their input was rejected.
if B > C:
    if D > A:
        if (C + D) > (A + B):
            if C > 0 and D > 0:
                if A % 2 == 0:
                    print("Valores aceitos")
                else:
                    # Failed at A % 2 == 0
                    print("Valores nao aceitos")
            else:
                # Failed at C > 0 and D > 0
                print("Valores nao aceitos")
        else:
            # Failed at (C + D) > (A + B)
            print("Valores nao aceitos")
    else:
        # Failed at D > A
        print("Valores nao aceitos")
else:
    # Failed at B > C
    print("Valores nao aceitos")



