from os import system

if __name__ == '__main__':
    system('cls')
    
    decimal = int(input('Ingresa numero base diez '))
    
    x = decimal
    while x>0:
        print(x%2, end='')
        x //= 2
