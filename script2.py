from arbolBinario.arbol import Arbol
from arbolBinario.nodo import Nodo

def problemaDelcamiante():
    posibleValle=False
    recorridoT=0
    vallesT=0
    print("Ingrese el camino recorrido:")
    print("Recuerde que la unica entrada vaida son U y D.")
    print("Omita anadir espacios.")
    ruta = input()
    ## Necesitamos regresar los valles, es decir cuando regresa a nivel del mar 
    for letra in ruta :
        if letra == "U" and posibleValle==False:
            recorridoT += 1
        elif letra == "U" and posibleValle==True:
            recorridoT += 1
            if recorridoT == 0:
                vallesT+=1
                posibleValle = False
        elif letra == "D" and posibleValle==False:
            recorridoT -= 1
            if recorridoT <= 0:
                posibleValle=True
        elif letra == "D" and posibleValle==True:
            recorridoT -= 1
        else:
            print("Cadena incorrecta")
            return 0
    print("Hubo un total de: ", vallesT)
    return vallesT

    


if __name__ == '__main__':
    nodoPrueba = Nodo(5)
    arbol = Arbol(nodoPrueba)
    arbol.agregarNodo(Nodo(3))
    arbol.agregarNodo(Nodo(5))
    arbol.agregarNodo(Nodo(7))
    arbol.agregarNodo(Nodo(2))
    arbol.agregarNodo(Nodo(20))
    arbol.agregarNodo(Nodo(1))
    arbol.agregarNodo(Nodo(6))
    print(arbol)