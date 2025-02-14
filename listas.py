from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Cuantos? '))
    V = []
    for i in range(n):
        dato = randrange(-100, 101)
        V.append(dato)
        print(f'V[{i}] = {V[i]}')
    print('\n')

    s = 0
    for i in range(n):
        s = s+V[i]
        #print(f'V[{i}] = {V[i]}\ts={s}')
    #print('\n')
        
    print(f's={s}')
    if n>0:
        promedio = s/n
        print(f'promedio = {promedio}')
    
    menor = V[0]
    posMenor = 0
    for i in range(n):
        #print(f'menor = {menor}')
        if V[i] < menor:
            menor = V[i]
            posMenor = i
    #print('\n')
    print(f'menor = {menor} = V[{posMenor}]')

    mayor = V[0]
    posMayor = 0
    for i in range(n):
        #print(f'mayor = {mayor}')
        if V[i] > mayor:
            mayor = V[i]
            posMayor = i
    #print('\n')
    print(f'mayor = {mayor} = V[{posMayor}]')

    menoresQuePromedio = 0
    for i in range(n):
        if V[i] < promedio:
            menoresQuePromedio += 1
    print(f'Hay {menoresQuePromedio} datos menores al promedio')

    mayoresQuePromedio = 0
    for i in range(n):
        if V[i] > promedio:
            mayoresQuePromedio += 1
    print(f'Hay {mayoresQuePromedio} datos mayores al promedio')
