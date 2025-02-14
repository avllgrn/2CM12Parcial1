from os import system

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Cuantos? '))
    s = 0
    
    for i in range(n):
        s = s+i
        print(f'i={i}\ts={s}')
        