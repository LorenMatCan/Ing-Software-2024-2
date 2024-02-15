from arbolBinario.nodo import Nodo
class Arbol:
    """
    Clase que representa un arbol binario
    """

    def __init__(self, raiz):
        self.raiz = raiz

    def obtener_raiz(self):
        return self.raiz

    def agregar_nodo(self, nodo):
        if self.raiz == None:
            self.raiz = nodo
        else:
            self.agregar_nodo_recursivo(self.raiz, nodo)

    def agregar_nodo_recursivo(self, raiz, nodo):
        if raiz == None:
            raiz = nodo
        if nodo.obtener_valor() <= raiz.obtener_valor():
            if raiz.obtener_izq() == None:
                raiz.asignar_izq(nodo)
            else:
                self.agregar_nodo_recursivo(raiz.obtener_izq(), nodo)
        else:
            if raiz.obtener_der() == None:
                raiz.asignar_der(nodo)
            else:
                self.agregar_nodo_recursivo(raiz.obtener_der(), nodo)

    def __str__(self):
        cadena = ""
        if self.raiz != None:
            cadena = self.str_recursivo(self.raiz)
        return cadena

    def str_recursivo(self, raiz):
        cadena = ""
        if raiz.obtener_izq() != None:
            cadena += "(izq :"+self.str_recursivo(raiz.obtener_izq())+") "
        cadena += str(raiz) + " "
        if raiz.obtener_der() != None:
            cadena += "(der: " + self.str_recursivo(raiz.obtener_der())+")"
        return cadena

    def recorrido_inorden(self):
         return self.recorrido_inorden_recursivo(self.raiz)
        

    def recorrido_inorden_recursivo(self, raiz, lista = []):
        if raiz != None:
            self.recorrido_inorden_recursivo(raiz.obtener_izq())
            lista.append(raiz.obtener_valor())
            self.recorrido_inorden_recursivo(raiz.obtener_der())
        return lista

    
    def recorrido_preorden(self):
        return self.recorrido_preorden_recursivo(self.raiz)

    def recorrido_preorden_recursivo(self, raiz, lista = []):
        if raiz != None:
            lista.append(raiz.obtener_valor())
            self.recorrido_preorden_recursivo(raiz.obtener_izq())
            self.recorrido_preorden_recursivo(raiz.obtener_der())
        return lista

    def recorrido_postorden(self):
        return self.recorrido_postorden_recursivo(self.raiz)

    def recorrido_postorden_recursivo(self, raiz, lista = []):
        if raiz != None:
            self.recorrido_postorden_recursivo(raiz.obtener_izq())
            self.recorrido_postorden_recursivo(raiz.obtener_der())
            lista.append(raiz.obtener_valor())
        return lista





