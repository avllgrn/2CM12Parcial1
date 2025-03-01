from os import system

if __name__ == '__main__':
    system('cls')

    d = {}
    print(d, type(d), len(d))   # muestra el diccionario
    print(d.items(), type(d.items()), len(d.items()))   # muestra los elementos del diccionario (lista de tuplas)
    for i in d.items():
        print(i, type(i))   # muestra cada item/tupla/pareja
    print()

    for k,v in d.items():
        print(k, type(k), ', ', v, type(v))   # muestra cada clave y valor de cada item/tupla/pareja
    print()


    d1 = {'clave1':1}
    print(d1, type(d1), len(d1))    # muestra el diccionario
    print(d1.items(), type(d1.items()), len(d1.items()))    # muestra los elementos del diccionario (lista de tuplas)
    for i in d1.items():
        print(i, type(i))   # muestra cada item/tupla/pareja
    print()

    for k,v in d1.items():
        print(k, type(k), ', ', v, type(v))# muestra cada clave y valor de cada item/tupla/pareja
    print()

    d2 = {'clave1':1, 'clave2':2}
    print(d2, type(d2), len(d2))    # muestra el diccionario
    print(d2.items(), type(d2.items()), len(d2.items()))    # muestra los elementos del diccionario (lista de tuplas)
    for i in d2.items():
        print(i, type(i))   # muestra cada item/tupla/pareja
    print()

    for k,v in d2.items():
        print(k, type(k), ', ', v, type(v))# muestra cada clave y valor de cada item/tupla/pareja
    print()

    d3 = {'clave1':1, 'clave2':2, 'clave3':3}
    print(d3, type(d3), len(d3))    # muestra el diccionario
    print(d3.items(), type(d3.items()), len(d3.items()))    # muestra los elementos del diccionario (lista de tuplas)
    for i in d3.items():
        print(i, type(i))   # muestra cada item/tupla/pareja
    print()

    for k,v in d3.items():
        print(k, type(k), ', ', v, type(v))# muestra cada clave y valor de cada item/tupla/pareja
    print()
    