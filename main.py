# TRES EN RAYA POR xLune64

def comprobarX(tablero):
    for j in range(len(tablero)):
        comprobacion = [tablero[j][0], tablero[j][1], tablero[j][2]]
        if (comprobacion[0] == comprobacion[1] == comprobacion[2]) and comprobacion[0] != " ":
            print("TRES EN RAYA: Fila", j+1, "para jugador", comprobacion[0])
            return True
    return False

def comprobarY(tablero):
    for j in range(len(tablero)):
        comprobacion = [tablero[0][j], tablero[1][j], tablero[2][j]]
        if (comprobacion[0] == comprobacion[1] == comprobacion[2]) and comprobacion[0] != " ":
            print("TRES EN RAYA: Columna", j+1, "para jugador", comprobacion[0])
            return True
    return False

def comprobarDiagonal(tablero):
    comprobacion = []
    for j in range(len(tablero)):
        comprobacion.append(tablero[j][j])
    if (comprobacion[0] == comprobacion[1] == comprobacion[2]) and comprobacion[0] != " ":
        print("TRES EN RAYA: Digonal izq arriba a der abajo para jugador", tablero[0][j])
        return True

    comprobacion = []
    comprobacion.append(tablero[0][2])
    comprobacion.append(tablero[1][1])
    comprobacion.append(tablero[2][0])
    if (comprobacion[0] == comprobacion[1] == comprobacion[2]) and comprobacion[0] != " ":
        print("TRES EN RAYA: Digonal izq abajo a der arriba para jugador", tablero[0][j])
        return True
    return False

def comprobarTablero(tablero):
    if (comprobarX(tablero) or comprobarY(tablero) or comprobarDiagonal(tablero)):
        return True
    return False
    
    

def imprimirTablero(tablero):
    print("  | 1 | 2 | 3")
    print("1 |", tablero[0][0],"|",tablero[0][1],"|",tablero[0][2])
    print("2 |", tablero[1][0],"|",tablero[1][1],"|",tablero[1][2])
    print("3 |", tablero[2][0],"|",tablero[2][1],"|",tablero[2][2])
    print("--------------")

def preguntarJugadorX(tablero):
    try:
        respuestaX = int(input("Dime nº de fila: "))
        respuestaY = int(input("Dime nº de columna: "))
        if (tablero[respuestaX-1][respuestaY-1] == " "):
            tablero[respuestaX-1][respuestaY-1] = "X"
            return tablero
        else:
            print("Esa coordenada no está vacía")
            preguntarJugadorX(tablero)
            return tablero
    except:
        print("Coordenadas incorrectas")
        preguntarJugadorX(tablero)
        return tablero

def preguntarJugadorO(tablero):
    try:
        respuestaX = int(input("Dime nº de fila: "))
        respuestaY = int(input("Dime nº de columna: "))
        if (tablero[respuestaX-1][respuestaY-1] == " "):
            tablero[respuestaX-1][respuestaY-1] = "O"
            return tablero
        else:
            print("Esa coordenada no está vacía")
            preguntarJugadorO(tablero)
            return tablero
    except:
        print("Coordenadas incorrectas")
        preguntarJugadorO(tablero)
        return tablero

def vaciarTablero(tablero):
    tablero = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
    return tablero

tablero = []
tablero = vaciarTablero(tablero)
respuesta = "s"
while (respuesta == "s"):
    imprimirTablero(tablero)
    tablero = preguntarJugadorX(tablero)
    if (comprobarTablero(tablero)):
        print("PARTIDA TERMINADA")
        imprimirTablero(tablero)
        respuesta = input("¿Quieres volver a jugar? (s/n) ")
        print("--------------")
        tablero = vaciarTablero(tablero)
        continue
    imprimirTablero(tablero)
    tablero = preguntarJugadorO(tablero)
    if (comprobarTablero(tablero)):
        print("PARTIDA TERMINADA")
        imprimirTablero(tablero)
        respuesta = input("¿Quieres volver a jugar? (s/n) ")
        print("--------------")
        tablero = vaciarTablero(tablero)
        continue