from ClaseNodo import ClaseNodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def InsertarNodo(self, valor):
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    def _insertarRecursivo(self, nodo, valor):
        #caso base
        if nodo is None:
            return ClaseNodo(valor)
        if valor < nodo.getValor():
            nodo.setHijoIzquierdo(self._insertarRecursivo(nodo.getHijoIzquierdo(), valor))
        else:
            nodo.setHijoDerecho(self._insertarRecursivo(nodo.getHijoDerecho(), valor))
        return nodo

    def EsVacio(self):
        return self.raiz is None

    def EsHoja(self, nodo):
        if nodo is None:
            return False
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None

    def BuscarX(self, valor):
        return self._buscarRecursivo(self.raiz, valor)

    def _buscarRecursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor == nodo.getValor():
            return nodo
        elif valor < nodo.getValor():
            return self._buscarRecursivo(nodo.getHijoIzquierdo(), valor)
        else:
            return self._buscarRecursivo(nodo.getHijoDerecho(), valor)

    def InOrden(self):
        self._inOrdenRecursivo(self.raiz)
        print()

    def _inOrdenRecursivo(self, nodo):
        if nodo is not None:
            self._inOrdenRecursivo(nodo.getHijoIzquierdo())
            print(nodo.getValor(), end=" ")
            self._inOrdenRecursivo(nodo.getHijoDerecho())

    def PreOrden(self):
        self._preOrdenRecursivo(self.raiz)
        print()

    def _preOrdenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo.getValor(), end=" ")
            self._preOrdenRecursivo(nodo.getHijoIzquierdo())
            self._preOrdenRecursivo(nodo.getHijoDerecho())

    def PostOrden(self):
        self._postOrdenRecursivo(self.raiz)
        print()

    def _postOrdenRecursivo(self, nodo):
        if nodo is not None:
            self._postOrdenRecursivo(nodo.getHijoIzquierdo())
            self._postOrdenRecursivo(nodo.getHijoDerecho())
            print(nodo.getValor(), end=" ")


if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.InsertarNodo(100)
    arbol1.InsertarNodo(90)
    arbol1.InsertarNodo(120)
    arbol1.InsertarNodo(70)
    arbol1.InsertarNodo(75)
    arbol1.InsertarNodo(130)
    arbol1.InsertarNodo(200)

    print("¿El árbol está vacío?:", arbol1.EsVacio())

    print("Recorrido InOrden:")
    arbol1.InOrden()

    print("Recorrido PreOrden:")
    arbol1.PreOrden()

    print("Recorrido PostOrden:")
    arbol1.PostOrden()

    buscado = 75
    nodo = arbol1.BuscarX(buscado)
    if nodo:
        print(f"Valor {buscado} encontrado. ¿Es hoja?:", arbol1.EsHoja(nodo))
    else:
        print(f"Valor {buscado} no encontrado.")



