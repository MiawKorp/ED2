from ClaseNodo import ClaseNodo

class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    def _insertarRecursivo(self, raizAux, valor):
        # Caso Base
        if raizAux is None:
            raizAux = ClaseNodo(valor)
            return raizAux
        else:
            if valor < raizAux.getValor():
                raizAux.setHijoIzquierdo(
                    self._insertarRecursivo(raizAux.getHijoIzquierdo(), valor)
                )
            else:
                raizAux.setHijoDerecho(
                    self._insertarRecursivo(raizAux.getHijoDerecho(), valor)
                )
            return raizAux

    def contarNodos(self):
        return self._contarNodosRecursivo(self.raiz)

    def _contarNodosRecursivo(self, raizAux):
        if raizAux is None:
            return 0
        return (1
                + self._contarNodosRecursivo(raizAux.getHijoIzquierdo())
                + self._contarNodosRecursivo(raizAux.getHijoDerecho()))

    def isVacio(self):
        return self.raiz is None


if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(90)
    arbol1.insertar(120)
    arbol1.insertar(70)
    arbol1.insertar(75)
    arbol1.insertar(130)
    arbol1.insertar(200)

    print("Cantidad de nodos:", arbol1.contarNodos())



