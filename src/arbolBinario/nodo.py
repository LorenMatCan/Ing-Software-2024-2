class Nodo :
    """
    clase auxiliar nodo para arbol binario
    """
    
    def __init__(self, valor, izq = None, der = None) :
        self.valor = valor
        self.izq = izq
        self.der = der 
    
    def __str__(self) :
        return str(self.valor)

    def obtener_valor(self) :
        return self.valor

    def obtener_izq(self) :
        return self.izq
    
    def obtener_der(self) :
        return self.der
    
    def asignar_izq(self, izq) :
        self.izq = izq

    def asignar_der(self, der) :
        self.der = der


    