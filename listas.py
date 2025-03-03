from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    dias = {1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado', 7:'Domingo'}
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    for d in range(1, 8):
        print(dias.get(d), dias[d])
    print()

    for m in range(1, 13):
        print(meses.get(m), meses[m])
    print()
