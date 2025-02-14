from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Cuantos? '))
    s = 0
    for i in range(n+1):
        dato = randrange(-100, 101)
        s = s+dato
        print(f'i={dato}\ts={s}')
        
    print(f's={s}')
