class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__hijo_izquierdo = None
        self.__hijo_derecho = None

    def get_valor(self):
        return self.__valor

    def get_hijo_izquierdo(self):
        return self.__hijo_izquierdo

    def get_hijo_derecho(self):
        return self.__hijo_derecho

    def set_valor(self, valor):
        self.__valor = valor

    def set_hijo_izquierdo(self, nodo):
        self.__hijo_izquierdo = nodo

    def set_hijo_derecho(self, nodo):
        self.__hijo_derecho = nodo


class ArbolBinario:
    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, nodo):
        self.__raiz = nodo

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.__raiz is None:
            self.__raiz = nuevo
            return

        actual = self.__raiz
        while True:
            if valor < actual.get_valor():
                if actual.get_hijo_izquierdo() is None:
                    actual.set_hijo_izquierdo(nuevo)
                    break
                else:
                    actual = actual.get_hijo_izquierdo()
            else:
                if actual.get_hijo_derecho() is None:
                    actual.set_hijo_derecho(nuevo)
                    break
                else:
                    actual = actual.get_hijo_derecho()

    def buscar(self, valor):
        actual = self.__raiz
        while actual:
            if valor == actual.get_valor():
                return True
            elif valor < actual.get_valor():
                actual = actual.get_hijo_izquierdo()
            else:
                actual = actual.get_hijo_derecho()
        return False

    def recorrer_en_orden(self):
        resultado = []
        pila = []
        actual = self.__raiz

        while pila or actual:
            if actual:
                pila.append(actual)
                actual = actual.get_hijo_izquierdo()
            else:
                actual = pila.pop()
                resultado.append(actual.get_valor())
                actual = actual.get_hijo_derecho()
        return resultado

    def contar_nodos(self):
        if self.__raiz is None:
            return 0

        pila = [self.__raiz]
        contador = 0

        while pila:
            nodo = pila.pop()
            contador += 1
            if nodo.get_hijo_derecho():
                pila.append(nodo.get_hijo_derecho())
            if nodo.get_hijo_izquierdo():
                pila.append(nodo.get_hijo_izquierdo())

        return contador

if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(90)
    arbol1.insertar(120)
    arbol1.insertar(70)
    arbol1.insertar(75)
    arbol1.insertar(130)
    arbol1.insertar(200)

    print("Recorrido en orden:", arbol1.recorrer_en_orden())
    print("Cantidad de nodos:", arbol1.contar_nodos())
    print("¿Está el 75?", arbol1.buscar(75))
    print("¿Está el 50?", arbol1.buscar(50))
