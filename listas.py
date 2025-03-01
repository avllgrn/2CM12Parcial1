from os import system

if __name__ == '__main__':
    system('cls')

    d = {}
    print(d, type(d), len(d), '\n') # muestra el diccionario
    
    d.update({'clave1':'valor1'})
    print(d, type(d), len(d), '\n') # muestra el diccionario
    
    d.update({'clave2':'valor2'})
    print(d, type(d), len(d), '\n') # muestra el diccionario

    d.update({'clave3':'valor3'})
    print(d, type(d), len(d), '\n') # muestra el diccionario
    
    print(d.items())    # muestra los elementos del diccionario (lista de tuplas)
    for i in d.items(): 
        print(i, type(i))    # muestra cada item/tupla/pareja
    print()

    for k,v in d.items(): 
        print(k, type(k), ', ', v, type(v))    # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
    print()

    print(d.keys()) # muestra cada clave de cada item/tupla/pareja
    for k in d.keys():
        print(k, type(k))
    print()

    print(d.values())   # muestra cada valor de cada item/tupla/pareja
    for v in d.values():
        print(v, type(v))
    
    