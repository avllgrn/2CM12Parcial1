from os import system

if __name__ == '__main__':
    system('cls')

    dias = {1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves', 5:'Viernes', 6:'Sábado', 7:'Domingo'}
    print(dias, type(dias), len(dias), '\n') # muestra el diccionario
    
    print(dias.items())    # muestra los elementos del diccionario (lista de tuplas)
    for i in dias.items(): 
        print(i, type(i))    # muestra cada item/tupla/pareja
    print()

    for k,v in dias.items(): 
        print(k, type(k), ', ', v, type(v))    # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
    print()

    print(dias.keys()) # muestra cada clave de cada item/tupla/pareja
    for k in dias.keys():
        print(k, type(k))
    print()

    print(dias.values())   # muestra cada valor de cada item/tupla/pareja
    for v in dias.values():
        print(v, type(v))
    
    