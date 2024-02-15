import random

def jugadorValido(jugador, primerjugador, segundojugador):
    """
    Revisa que el nombre ingresado sea valido
    """
    if jugador == primerjugador or jugador == segundojugador:
        return True
    else:
        print("Jugador invalido, favor de ingresar el nombre del jugador que gana el punto: ")
        return False

def finJuego(puntosPrimerJugador, puntosSegundoJugador,x):
    """
    Revisa si el juego o el set ha terminado
    """
    if puntosPrimerJugador >= x and puntosPrimerJugador >= puntosSegundoJugador + 2:
        return True
    if puntosSegundoJugador >= x and puntosSegundoJugador >= puntosPrimerJugador + 2:
        return True
    return False

def puntosAMarcador(punto,ventaja):
    """
    Convierte los puntos del partivo a una puntucion valida segun las reglas del tenis 
    """
    if punto == 0:
        return "0"
    if punto == 1:
        return "15"
    if punto == 2:
        return "30"
    if punto == 3:
        return "40"
    if punto >= 4 and ventaja == True:
        return "Ventaja"
    if punto >= 4 and ventaja == False:
        return "40"

def marcarPuntos(puntosPrimerJugador, puntosSegundoJugador,ventajaPrimerJugador,ventajaSegundoJugador):
    """
    Función auxiliar que imprime el marcador del juego
    """
    print ("Marcador: ", puntosAMarcador(puntosPrimerJugador,ventajaPrimerJugador), "-", puntosAMarcador(puntosSegundoJugador,ventajaSegundoJugador))

def ganador(puntosPrimerJugador, puntosSegundoJugador,primerjugador,segundojugador,tipoganador="Juego"):
    """
    Compara los marcadores y anuncia quien es el ganador
    """
    if puntosPrimerJugador > puntosSegundoJugador:
        print("El ganador del ", tipoganador, "es: ", primerjugador)
        return primerjugador
    else:
        print("El ganador del ", tipoganador, "es: ", segundojugador)
        return segundojugador

def juego(primerjugador, segundojugador,saque):
    """
    Función principal que simula un juego de tenis
    """
    puntosPrimerJugador = 0
    puntosSegundoJugador = 0
    ventajaPrimerJugador = False ## Variable que nos ayuda a marcar quien tiene ventaja
    ventajaSegundoJugador = False ## Variable que nos ayuda a marcar quien tiene ventaja
    terminado = False
    deuce = False

    while not terminado: 
        print( saque, "Realiza el saque")
        print("Ingrese el jugador que gana el punto: ")
        punto = ""
        valido = False
        while not valido:
            punto = input()
            valido = jugadorValido(punto, primerjugador, segundojugador)

        if punto == primerjugador:
            puntosPrimerJugador += 1
            if deuce == True:
                deuce = False
                ventajaPrimerJugador = True
                ventajaSegundoJugador = False

        else:
            puntosSegundoJugador += 1
            if deuce == True:
                deuce = False
                ventajaSegundoJugador = True
                ventajaPrimerJugador = False
        
        if puntosPrimerJugador >= 3 and puntosSegundoJugador >= 3 and puntosPrimerJugador == puntosSegundoJugador:
            print("Deuce")
            deuce = True
            ventajaPrimerJugador = False
            ventajaSegundoJugador = False
        
        marcarPuntos(puntosPrimerJugador, puntosSegundoJugador,ventajaPrimerJugador,ventajaSegundoJugador)
        
        terminado = finJuego(puntosPrimerJugador, puntosSegundoJugador,4)
        
    return ganador(puntosPrimerJugador, puntosSegundoJugador,primerjugador,segundojugador)

def saqueF(primerjugador, segundojugador, actual):
    """
    Cambia el saque
    """
    if actual == primerjugador:
        return segundojugador
    else:
        return primerjugador

def setTenis(primerjugador, segundojugador):
    """
    Función principal que simula el marcador de un set de tenis
    """
    puntosPrimerJugador = 0
    puntosSegundoJugador = 0
    numeroJuegos = 0
    terminado = False
    saque = random.choice([primerjugador, segundojugador])
    while not terminado:
        ganadorj = juego(primerjugador, segundojugador,saque)
        saqueO= saque
        saque = saqueF(primerjugador, segundojugador, saqueO)
        if ganadorj == primerjugador:
            puntosPrimerJugador += 1
        else:
            puntosSegundoJugador += 1
        numeroJuegos += 1
        terminado = finJuego(puntosPrimerJugador, puntosSegundoJugador,6)
        print("Marcador del set: ", puntosPrimerJugador, "-", puntosSegundoJugador)
    ganadorSet = ganador(puntosPrimerJugador, puntosSegundoJugador,primerjugador,segundojugador, "Set")
    return ganadorSet , numeroJuegos

def cambioCancha(numeroJuegos):
    if numeroJuegos % 2 != 0:
        print("Cambio de cancha")

def finJuegoTotal(primerJugador,segundojugador,puntosPrimerJugador,puntosSegundoJugador):
    """
    Revisa si el partido ha terminado
    """

    if puntosPrimerJugador == 2:
        print("El jugador ", primerJugador, "ha ganado el partido")
        return True
    elif puntosSegundoJugador == 2:
        print("El jugador ", primerJugador, "ha ganado el partido")
        return True
    elif puntosPrimerJugador == puntosSegundoJugador == 1 :
        return False
    else:
        return False


def juegoASets(primerJugador, segundoJugador):
    """
    Función principal que simula un partido de tenis a 3 sets
    """
    
    terminado = False
    puntosPrimerJugador = 0
    puntosSegundoJugador = 0 
    setA=0
    while not terminado:
        print("Set actual: ",setA)
        resultados = setTenis(primerJugador,segundoJugador)
        cambioCancha(resultados[1])
        if (resultados[0]==primerJugador):
            puntosPrimerJugador += 1
        else:
            puntosSegundoJugador += 1
        setA+=1
        print("Marcador del juego: ", puntosPrimerJugador, "-", puntosSegundoJugador)
        terminado = finJuegoTotal(primerJugador,segundoJugador,puntosPrimerJugador,puntosSegundoJugador)
    

def juegoTenis():
    print("Marcador de puntos de juego de tenis /n")
    print("Para empezar es necesario que ingrese el nombre de los jugadores")
    print("Favor de evitar el uso de acentos y caracteres especiales.")
    print("El programa es sensible a mayúsculas y minúsculas.")
    print("Ingrese el nombre del primer jugador: ")
    jugador1 = input()
    print("Ingrese el nombre del segundo jugador: ")
    jugador2 = input()
    print("El juego ha comenzado entre", jugador1, "y", jugador2)
    juegoASets(jugador1, jugador2)


if __name__ == '__main__':
    juegoTenis()
    