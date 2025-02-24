from os import system

def muestraContenedor(l):
    tam = len(l)
    for i in range(tam):
        print(f'[{i}] = {l[i]}')

if __name__ == '__main__':
    system('cls')

    lista = [1, 3, 5, 7, 9]
    tupla = (2, 4, 6, 8, 10)

    print(f'lista{lista}, {type(lista)}, tam {len(lista)}')
    muestraContenedor(lista)
    print()

    print(f'tupla{tupla}, {type(tupla)}, tam {len(tupla)}')
    muestraContenedor(tupla)
    print()
