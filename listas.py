from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    dias = {1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado', 7:'Domingo'}
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    n = int(input('Cuántos valores? '))

    with open('datos.txt','w') as archivo:
        for i in range(n):
            d = randrange(1,8)
            m = randrange(1,13)
            archivo.writelines(str(d)+', '+str(m) + '\n')
            print(dias.get(d), 'de', meses.get(m))
    print('\n')

    with open('datos.txt','r') as archivo:
        for i in range(n):
            linea = archivo.readline().strip().split(',')
            #print(linea)
            d = int(linea[0])
            m = int(linea[1])
            print(dias.get(d), 'de', meses.get(m))
    print('\n')
