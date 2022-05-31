
# Online Python - IDE, Editor, Compiler, Interpreter
"""Ejercicio 4"""

print("Welcome to fun with flags")
print("*************************")
print("\n")
H=0
L=0

while((H>2 or H<20) and H%2==0):
    H = int(input("Enter the height you want: "))


while((L>2 or L<20) and L%2==0):
    L = int(input("Enter the length you want: "))


for row in range(H):
    if row!=int(H/2):
        for column in range(L):
            if column==int(L/2):
                print('+', end='')
            else:
                print("0",end='')
    else:
        for column in range(L):
            print('+', end='')
    print('')



