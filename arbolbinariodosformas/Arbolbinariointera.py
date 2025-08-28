from ClaseNodo import ClaseNodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def InsertarNodo(self, valor):
        nuevo = ClaseNodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if valor < actual.getValor():
                if actual.getHijoIzquierdo() is None:
                    actual.setHijoIzquierdo(nuevo)
                    break
                else:
                    actual = actual.getHijoIzquierdo()
            else:
                if actual.getHijoDerecho() is None:
                    actual.setHijoDerecho(nuevo)
                    break
                else:
                    actual = actual.getHijoDerecho()

    def EsVacio(self):
        return self.raiz is None

    def EsHoja(self, nodo):
        if nodo is None:
            return False
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None

    def BuscarX(self, valor):
        actual = self.raiz
        while actual is not None:
            if valor == actual.getValor():
                return actual
            elif valor < actual.getValor():
                actual = actual.getHijoIzquierdo()
            else:
                actual = actual.getHijoDerecho()
        return None

    def InOrden(self):
        stack = []
        actual = self.raiz
        while stack or actual:
            if actual:
                stack.append(actual)
                actual = actual.getHijoIzquierdo()
            else:
                actual = stack.pop()
                print(actual.getValor(), end=" ")
                actual = actual.getHijoDerecho()
        print()

    def PreOrden(self):
        if self.raiz is None:
            return
        stack = [self.raiz]
        while stack:
            nodo = stack.pop()
            print(nodo.getValor(), end=" ")
            if nodo.getHijoDerecho():
                stack.append(nodo.getHijoDerecho())
            if nodo.getHijoIzquierdo():
                stack.append(nodo.getHijoIzquierdo())
        print()

    def PostOrden(self):
        if self.raiz is None:
            return
        stack1 = [self.raiz]
        stack2 = []
        while stack1:
            nodo = stack1.pop()
            stack2.append(nodo)
            if nodo.getHijoIzquierdo():
                stack1.append(nodo.getHijoIzquierdo())
            if nodo.getHijoDerecho():
                stack1.append(nodo.getHijoDerecho())
        while stack2:
            nodo = stack2.pop()
            print(nodo.getValor(), end=" ")
        print()

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
