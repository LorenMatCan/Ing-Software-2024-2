import random

def jugadorValido(jugador, primerjugador, segundojugador):
    if jugador == primerjugador or jugador == segundojugador:
        return True
    else:
        print("Jugador invalido, favor de ingresar el nombre del jugador que gana el punto: ")
        return False

def finJuego(puntosPrimerJugador, puntosSegundoJugador,x):
    if puntosPrimerJugador >= x and puntosPrimerJugador >= puntosSegundoJugador + 2:
        return True
    if puntosSegundoJugador >= x and puntosSegundoJugador >= puntosPrimerJugador + 2:
        return True
    return False

def puntosAMarcador(punto,ventaja):
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
    print ("Marcador: ", puntosAMarcador(puntosPrimerJugador,ventajaPrimerJugador), "-", puntosAMarcador(puntosSegundoJugador,ventajaSegundoJugador))

def ganador(puntosPrimerJugador, puntosSegundoJugador,primerjugador,segundojugador,tipoganador="Juego"):
    if puntosPrimerJugador > puntosSegundoJugador:
        print("El ganador del ", tipoganador, "es: ", primerjugador)
        return primerjugador
    else:
        print("El ganador del ", tipoganador, "es: ", segundojugador)
        return segundojugador

def juego(primerjugador, segundojugador,saque):
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
        if actual == primerjugador:
            return segundojugador
        else:
            return primerjugador

def setTenis(primerjugador, segundojugador):
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
        print("Marcador: ", puntosPrimerJugador, "-", puntosSegundoJugador)
    ganador = ganador(puntosPrimerJugador, puntosSegundoJugador,primerjugador,segundojugador, "Set")
    return ganador , numeroJuegos


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
    setTenis(jugador1, jugador2)


if __name__ == '__main__':
    juegoTenis()
    