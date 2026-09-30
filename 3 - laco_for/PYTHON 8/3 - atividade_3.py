import os
import time
os.system('cls')

num = int(input('Digite o número inteiro escolhido: '))
for i in range(num, 0, -1):
    print(i)
    time.sleep(1)