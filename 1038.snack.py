"""
Using the following table,
write a program that reads a code and the amount of an item.
After, print the value to pay.
This is a very simple program with the only intention of practice of selection commands.
====================================
code    []    Specification     []  price
1       []    Cachorro Quente   []  R$4.00
2       []    X-Salada          []  R$4.50
3       []    X-bacon           []  R$5.00
4       []    Torrada Simples   []  R$2.00
5       []    Refrigerante      []  R$1.50

Input
The input file contains two integer numbers X and Y.
X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid,
with 2 digits after the decimal point.
"""

""" Solution (A) """
x , y =  map(int, input().strip().split() )  # Product Code

if x == 1:
    print(f"Total: R$ {(y * 4.00):.2f}")
elif x == 2:
    print(f"Total: R$ {(y * 4.50):.2f}")
elif x == 3:
    print(f"Total: R$ {(y * 5.00):.2f}")
elif x == 4:
    print(f"Total: R$ {(y * 2.00):.2f}")
elif x == 5:
    print(f"Total: R$ {(y * 1.50):.2f}")
else:
    print("Invalid code")

""" Solution (B) """
x, y = map(int, input().strip().split())

prices = {
1: 4.00,
2: 4.50,
3: 5.00,
4: 2.00,
5: 1.50
}

if x in prices:
    total = prices[x] * y
    print(f"Total: R$ {total:.2f}")
else:
    print("Invalid code")
