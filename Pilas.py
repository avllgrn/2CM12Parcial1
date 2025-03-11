from os import system

class Nodo:
    def __init__(self, dato=None, inferior=None):
        self.dato = dato
        self.inferior = inferior

    def __str__(self):
        cadena = '| '
        cadena += str(self.dato) + ' |'
        if self.inferior != None:
            cadena += ' -> '
        return cadena

class Pila:
    def __init__(self):
        self.tope = None

    def __del__(self):
        self.liberaMemoria()

    def liberaMemoria(self):
        while not self.estaVacia():
            print(self.pop())

    def estaVacia(self):
        return self.tope == None

    def push(self, dato):
        self.tope = Nodo(dato, self.tope)

    def pop(self):
        d = None
        if not self.estaVacia():
            d = self.tope.dato
            aux = self.tope
            self.tope = self.tope.inferior
            del aux
        return d

if __name__ == '__main__':
    system('cls')

    P = Pila()

    P.push(5)
    P.push(3)
    P.push(7)
    P.push(-4)

    print(P.pop())
    print(P.pop())
    
    P.push(9)

    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())