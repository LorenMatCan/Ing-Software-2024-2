from arbolBinario.arbol import Arbol
from arbolBinario.nodo import Nodo

def problema_camiante():
    """
    Funcion que dada una cadena de U y D, cuenta cuantos valles se recorrieron
    Sean los valles cuando bajamos del nivel del mar y regresamos a el.
    """
    posibleValle=False # Bandera para saber si estamos en un valle
    recorridoT=0 # Contador para saber en que nivel estamos
    vallesT=0 # Contador para saber cuantos valles se recorrieron

    print("Ingrese el camino recorrido:")
    print("Recuerde que la unica entrada vaida son U y D.")
    print("Omita añadir espacios.")
    ruta = input()
    ## Necesitamos regresar los valles, es decir cuando regresa a nivel del mar 
    for letra in ruta :
        if letra == "U" and posibleValle==False: # Al subir tenemos que fijarnos que no estemos en un posible valle 
            recorridoT += 1                      # Si no estamos en un valle podemos subir sin ninguna consideración extra.
        elif letra == "U" and posibleValle==True:
            recorridoT += 1
            if recorridoT == 0:  # Si llegamos a nivel del mar, entonces ya terminamos el valle
                vallesT+=1
                posibleValle = False # Reseteamos la bandera
        elif letra == "D" and posibleValle==False:  
            recorridoT -= 1 # Si bajamos es probable que lleguemos a un valle por lo cual es importamte revisar
            if recorridoT <= 0: # Si llegamos al nivel del mar o menor puede ser que estemos en un posibe valle
                posibleValle=True
        elif letra == "D" and posibleValle==True: # Si ya estamos en un valle solo bajamos
            recorridoT -= 1
        else:  
            print("Cadena incorrecta")
            return 0
    print("Hubo un total de: ", vallesT)
    return vallesT

    


"""
Ejemplo de arbol binario
if __name__ == '__main__':
    arbol = Arbol(Nodo(45))
    arbol.agregar_nodo(Nodo(23))
    arbol.agregar_nodo(Nodo(67))
    arbol.agregar_nodo(Nodo(12))
    arbol.agregar_nodo(Nodo(34))
    arbol.agregar_nodo(Nodo(56))
    arbol.agregar_nodo(Nodo(78))
    print(arbol)
    print(arbol.recorrido_inorden())
    print(arbol.recorrido_preorden())
    print(arbol.recorrido_postorden())
"""
    