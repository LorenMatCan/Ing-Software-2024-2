from arbolBinario.nodo import Nodo
class Arbol:

    def __init__(self, raiz):
        self.raiz = raiz

    def obtener_raiz(self):
        return self.raiz

    def agregarNodo(self, nodo):
        if self.raiz == None:
            self.raiz = nodo
        else:
            self.agregarNodoRecursivo(self.raiz, nodo)

    def agregarNodoRecursivo(self, raiz, nodo):
        if raiz == None:
            raiz = nodo
        if nodo.obtener_valor() <= raiz.obtener_valor():
            if raiz.obtener_izq() == None:
                raiz.asignar_izq(nodo)
            else:
                self.agregarNodoRecursivo(raiz.obtener_izq(), nodo)
        else:
            if raiz.obtener_der() == None:
                raiz.asignar_der(nodo)
            else:
                self.agregarNodoRecursivo(raiz.obtener_der(), nodo)

    def __str__(self):
        cadena = ""
        if self.raiz != None:
            cadena = self.strRecursivo(self.raiz)
        return cadena

    def strRecursivo(self, raiz):
        cadena = ""
        if raiz.obtener_izq() != None:
            cadena += "izq :"+self.strRecursivo(raiz.obtener_izq())
        cadena += str(raiz) + " "
        if raiz.obtener_der() != None:
            cadena += "der: " + self.strRecursivo(raiz.obtener_der())
        return cadena





