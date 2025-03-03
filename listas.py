from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    dias = {1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado', 7:'Domingo'}
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    n = int(input('Cuántos valores? '))
    for i in range(n):
        print(dias.get(randrange(1,8)), 'de', meses.get(randrange(1,13)))