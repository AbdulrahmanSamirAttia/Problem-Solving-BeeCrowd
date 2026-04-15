"""
Read a value of floating point with two decimal places.
This represents a monetary value. After this,
calculate the smallest possible number of notes and coins on which the value can be decomposed.
The considered notes are of 100, 50, 20, 10, 5, 2.
The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01.
Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
"""

""" Solution (A) """
amount = int(float(input().strip()) * 100)

print("NOTAS:")

# 100
banknote_100 = amount // 10000
amount = amount % 10000
print(f"{banknote_100} nota(s) de R$ 100.00")

# 50
banknote_50 = amount // 5000
amount = amount % 5000
print(f"{banknote_50} nota(s) de R$ 50.00")

# 20
banknote_20 = amount // 2000
amount = amount % 2000
print(f"{banknote_20} nota(s) de R$ 20.00")

# 10
banknote_10 = amount // 1000
amount = amount % 1000
print(f"{banknote_10} nota(s) de R$ 10.00")

# 5
banknote_5 = amount // 500
amount = amount % 500
print(f"{banknote_5} nota(s) de R$ 5.00")

# 2
banknote_2 = amount // 200
amount = amount % 200
print(f"{banknote_2} nota(s) de R$ 2.00")

print("MOEDAS:")

# 1
coin_1 = amount // 100
amount = amount % 100
print(f"{coin_1} moeda(s) de R$ 1.00")

# 0.50
coin_50 = amount // 50
amount = amount % 50
print(f"{coin_50} moeda(s) de R$ 0.50")

# 0.25
coin_25 = amount // 25
amount = amount % 25
print(f"{coin_25} moeda(s) de R$ 0.25")

# 0.10
coin_10 = amount // 10
amount = amount % 10
print(f"{coin_10} moeda(s) de R$ 0.10")

# 0.05
coin_05 = amount // 5
amount = amount % 5
print(f"{coin_05} moeda(s) de R$ 0.05")

# 0.01
coin_01 = amount
print(f"{coin_01} moeda(s) de R$ 0.01")


""" Solution (B) """
# amount = float(input().strip())
#
# print("NOTAS:")
# for val in [100, 50, 20, 10, 5, 2]:
#     print(f"{int(amount // val)} nota(s) de R$ {val}.00")
#     amount = round(amount % val, 2)
#
# print("MOEDAS:")
# for val in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
#     print(f"{int(amount / val)} moeda(s) de R$ {val:.2f}")
#     amount = round(amount % val, 2)



""" Solution (C) """
# amount = int( float(input().strip()) * 100 + 0.5 )
#
# print("NOTAS:")
# for val in [10000, 5000, 2000, 1000, 500, 200]:
#     print(f"{amount // val} nota(s) de R$ {val//100}.00")
#     amount %= val
#
# print("MOEDAS:")
# for val in [100, 50, 25, 10, 5, 1]:
#     print(f"{amount // val} moeda(s) de R$ {val // 100}.{val % 100 :02d}")
#     amount %= val
