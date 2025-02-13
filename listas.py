from os import system

def funcionParaEnteros():
    lista  = [12, 4, 65, -8, 10]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))


def funcionParaFlotantes():
    lista  = [1.2, 4.5, 6., -8.7]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

def funcionParaCadenas():
    lista  = [ 'puerta', 'casa','ventana']
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))




if __name__ == '__main__':
    system('cls')
    funcionParaEnteros()
    print()
    funcionParaFlotantes()
    print()
    funcionParaCadenas()
    print()
