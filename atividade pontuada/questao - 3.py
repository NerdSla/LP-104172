import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a == b:
    c = a + b
else:
    c = a * b

print(f'Primeiro número: {a}')
print(f'Segundo número: {b}')
print(f'Terceiro número: {c}')