from os import system

if __name__ == '__main__':
    system('cls')

    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    print(meses, type(meses), len(meses), '\n') # muestra el diccionario
    
    print(meses.items())    # muestra los elementos del diccionario (lista de tuplas)
    for i in meses.items(): 
        print(i, type(i))    # muestra cada item/tupla/pareja
    print()

    for k,v in meses.items(): 
        print(k, type(k), ', ', v, type(v))    # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
    print()

    print(meses.keys()) # muestra cada clave de cada item/tupla/pareja
    for k in meses.keys():
        print(k, type(k))
    print()

    print(meses.values())   # muestra cada valor de cada item/tupla/pareja
    for v in meses.values():
        print(v, type(v))
