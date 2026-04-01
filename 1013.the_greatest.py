"""
BeeCrowd Problem 1013 - The Greatest
Finds the largest of three integers using a specific formula.
"""

""" Solution (A) """
# 1. Input: Read three integers
# map(int, ...) converts the strings from split() into integers
a, b, c = map(int, input().split())

# 2. Calculation: Using the formula twice to find the greatest
# (a + b + abs(a - b)) // 2 finds the larger of two numbers
maior_ab = (a + b + abs(a - b)) // 2
maior_final = (maior_ab + c + abs(maior_ab - c)) // 2

# 3. Output: Match the exact BeeCrowd message format
print(f"{maior_final} eh o maior")
