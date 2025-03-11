from os import system

class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        cadena = '| '
        cadena += str(self.dato) + ' |'
        if self.siguiente != None:
            cadena += ' -> '
        return cadena

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __del__(self):
        self.liberaMemoria()

    def liberaMemoria(self):
        while not self.estaVacia():
            print(self.pop())

    def estaVacia(self):
        return self.primero == None and self.ultimo == None

    def push(self, dato):
        if self.estaVacia():
            self.ultimo = Nodo(dato, None)
            self.primero = self.ultimo
        else:
            self.ultimo.siguiente = Nodo(dato, None)
            self.ultimo = self.ultimo.siguiente

    def pop(self):
        d = None
        if not self.estaVacia():
            d = self.primero.dato 
            if self.primero != self.ultimo:
                aux = self.primero
                self.primero = self.primero.siguiente
                del aux
            else:
                del self.primero
                self.primero = None
                self.ultimo = None
        return d

if __name__ == '__main__':
    system('cls')

    C = Cola()

    C.push(5.1)
    C.push(3.1)
    C.push(7.1)
    C.push(-4.1)

    print(C.pop(), ' -> ', end='')
    print(C.pop(), ' -> ', end='')
    
    C.push(9.1)

    print(C.pop(), ' -> ', end='')
    print(C.pop(), ' -> ', end='')
    print(C.pop(), ' -> ', end='')