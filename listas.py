from os import system

def generaDiccASCII():
    ASCII = {}
    for i in range(256):
        ASCII.update({i:chr(i)})
    return ASCII

def muestraDiccASCII(A):
    print(f'ASCII\n{A}\n')  # muestra diccionario
    print()
    
    print(A.items(),'\n')   # muestra los elementos del diccionario (lista de tuplas)
    print()
    
    for i in A.items():     # muestra cada item/tupla/pareja
        print(i)
    print()
            
    for k,v in A.items():   # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(f'{k}\t{type(k)}\t{v}\t{type(v)}')
    print()
      
def generaDiccNumeros():
    Numeros = {}
    for i in range(48,58):
        Numeros.update({i:chr(i)})
    return Numeros

def muestraDiccNumeros(N):
    print(f'Números\n{N}\n')    # muestra diccionario
    print()
    
    print(N.items(),'\n')       # muestra los elementos del diccionario (lista de tuplas)
    print()
    
    for i in N.items():         # muestra cada item/tupla/pareja
        print(i)
    print()
        
    for k,v in N.items():       # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(f'{k}\t{type(k)}\t{v}\t{type(v)}')
    print()
        
def generaDiccMayusculas():
    Mayusculas = {}
    for i in range(65,91):
        Mayusculas.update({i:chr(i)})
    return Mayusculas

def muestraDiccMayusculas(M):
    print(f'Mayúsculas\n{M}\n') # muestra diccionario
    
    print(M.items(),'\n')       # muestra los elementos del diccionario (lista de tuplas)
    print()
    
    for i in M.items():         # muestra cada item/tupla/pareja
        print(i)
    print()
        
    for k,v in M.items():       # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(f'{k}\t{type(k)}\t{v}\t{type(v)}')
    print()
        
def generaDiccMinusculas():
    Minusculas = {}
    for i in range(97,123):
        Minusculas.update({i:chr(i)})
    return Minusculas

def muestraDiccMinusculas(m):
    print(f'Minúsculas\n{m}\n')   # muestra diccionario

    print(m.items(),'\n')       # muestra los elementos del diccionario (lista de tuplas)
    print()
    
    for i in m.items():         # muestra cada item/tupla/pareja
        print(i)
    print()
        
    for k,v in m.items():       # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(f'{k}\t{type(k)}\t{v}\t{type(v)}')
    print()
        
def generaDiccIngles():
    Ingles = {
        'Números' : generaDiccNumeros(),
        'Mayúsculas' : generaDiccMayusculas(),
        'Minúsculas' : generaDiccMinusculas()
    }
    return Ingles

def muestraDiccIngles(I):
    print(f'Inglés\n{I}\n') # muestra diccionario

    print(I.items(),'\n')   # muestra los elementos del diccionario (lista de tuplas)
    print()
    
    for i in I.items():     # muestra cada item/tupla/pareja
        print(i, '\n')
    print()
    
    for k,v in I.items():   # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(f'{k}\t{type(k)}\t{v}\t{type(v)}\n')

    for k,v in I.items():   # muestra cada clave y valor (despempaquetados) de cada item/tupla/pareja
        print(k)
        for valor in v:
            print(v.get(valor), v[valor])
        print()
        
def menu():
    print('1. ASCII')
    print('2. Números')
    print('3. Mayúsculas')
    print('4. Minúsculas')
    print('5. Inglés')
    print('6. Salir')
    return input('Cuál es tu opción? ')    

def casos(opcion):
    match opcion:
        case '1':
            A = generaDiccASCII()
            muestraDiccASCII(A)
            print()
            system('pause')
            del A

        case '2':
            N = generaDiccNumeros()
            muestraDiccNumeros(N)
            print()
            system('pause')
            del N
        case '3':
            M = generaDiccMayusculas()
            muestraDiccMayusculas(M)
            print()
            system('pause')
            del M
        case '4':
            m = generaDiccMinusculas()
            muestraDiccMinusculas(m)
            print()
            system('pause')
            del m
        case '5':
            I = generaDiccIngles()
            muestraDiccIngles(I)
            print()
            system('pause')
            del I
        case '6':
            print('Adiós!')
        case _:
            print('Opción inválida!')
            system('pause')

if __name__ == '__main__':
    system('cls')
    
    opcion = None
    while opcion!='6':
        system('cls')
        opcion = menu()
        casos(opcion)