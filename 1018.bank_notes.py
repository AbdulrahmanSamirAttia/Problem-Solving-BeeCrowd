"""
In this problem you have to read an integer value
and calculate the smallest possible number of banknotes in which the value may be decomposed.
The possible banknotes are 100, 50, 20, 10, 5, 2 and 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).


Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example.
Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.

Input Sample:
576

Output Sample
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

"""

""" Solution (A) """
amount = int(input().strip())
print(amount)

banknote_100 = amount // 100
amount = amount - (banknote_100 * 100)
print(f"{banknote_100} nota(s) de R$ 100,00")

banknote_50 = amount // 50
amount = amount - (banknote_50 * 50)
print(f"{banknote_50} nota(s) de R$ 50,00")

banknote_20 = amount // 20
amount = amount - (banknote_20 * 20)
print(f"{banknote_20} nota(s) de R$ 20,00")

banknote_10 = amount // 10
amount = amount - (banknote_10 * 10)
print(f"{banknote_10} nota(s) de R$ 10,00")

banknote_5 = amount // 5
amount = amount - (banknote_5 * 5)
print(f"{banknote_5} nota(s) de R$ 5,00")

banknote_2 = amount // 2
amount = amount - (banknote_2 * 2)
print(f"{banknote_2} nota(s) de R$ 2,00")

banknote_1 = amount // 1
amount = amount - (banknote_1 * 1)
print(f"{banknote_1} nota(s) de R$ 1,00")


""" Solution (B) """
amount = int(input().strip())
print(amount)

banknotes = [100, 50, 20, 10, 5, 2, 1]

for note in banknotes:
    count = amount // note
    amount %= note # Same as: amount = amount - (count * note)
    print(f"{count} nota(s) de R$ {note},00")



