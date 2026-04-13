"""
Read an integer value corresponding to a person's age (in days)
and print it in years, months and days,
followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation,
consider the whole year with 365 days and 30 days every month.
In the cases of test there will never be a situation that allows 12 months and some days,
like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example.


Input Sample	Output Sample
400             1 ano(s)
                1 mes(es)
                5 dia(s)

800             2 ano(s)
                2 mes(es)
                10 dia(s)

30              0 ano(s)
                1 mes(es)
                0 dia(s)

"""

""" Solution (A) """
age = int(input().strip())

# 1 year = 365 days
years = age // 365
age = age % 365

# 1 month = 30 days
months = age // 30
age = age % 30

# The rest of days
days = age // 1

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")


""" Solution (B) """
age = int(input().strip())
print(f"{age // 365} ano(s)\n{(age % 365) // 30} mes(es)\n{(age % 365) % 30} dia(s)")
