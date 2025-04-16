import random
from typing import List, Tuple  # https://docs.python.org/3/library/typing.html#typing.List

# Constantes
N: int = 10  # Tamaño del tablero
CANTIDAD_DISPAROS: int = 15  # Disparos permitidos
CANTIDAD_BARCOS: int = 5  # Barcos en el tablero

# Tipos
Tablero = List[List[bool]]  # https://docs.python.org/3/library/typing.html#typing.List


def crear_tablero(n: int) -> Tablero:
    """Crea un tablero de NxN con todos los valores en False (sin barco)"""
    return [[False for _ in range(n)] for _ in range(n)]


def ubicar_barcos(tablero: Tablero, cantidad_barcos: int) -> None:
    """Ubica barcos de una sola casilla en posiciones aleatorias del tablero"""
    colocados = 0
    while colocados < cantidad_barcos:
        fila = random.randint(0, N - 1)
        columna = random.randint(0, N - 1)
        if not tablero[fila][columna]:
            tablero[fila][columna] = True
            colocados += 1


def mostrar_tablero(tablero: Tablero, disparos: List[List[bool]]) -> None:
    """Muestra el tablero con los disparos realizados"""
    print("Tablero:")
    for i in range(N):
        fila = ""
        for j in range(N):
            if disparos[i][j]:
                if tablero[i][j]:
                    fila += "X "  # Acierto
                else:
                    fila += "O "  # Fallo
            else:
                fila += ". "  # Sin disparo
        print(fila)
    print()


def jugar():
    """Función principal del juego"""
    tablero: Tablero = crear_tablero(N)
    disparos: List[List[bool]] = crear_tablero(N)
    ubicar_barcos(tablero, CANTIDAD_BARCOS)

    aciertos = 0
    fallos = 0

    for intento in range(CANTIDAD_DISPAROS):
        print(f"Disparo {intento + 1} de {CANTIDAD_DISPAROS}")
        mostrar_tablero(tablero, disparos)

        try:
            fila = int(input(f"Ingresá la fila (0 a {N - 1}): "))
            columna = int(input(f"Ingresá la columna (0 a {N - 1}): "))
        except ValueError:
            print("Entrada inválida. Intentá de nuevo.")
            continue

        if not (0 <= fila < N and 0 <= columna < N):
            print("Coordenadas fuera de rango. Intentá de nuevo.")
            continue

        if disparos[fila][columna]:
            print("Ya disparaste ahí. Probá otra casilla.")
            continue

        disparos[fila][columna] = True
        if tablero[fila][columna]:
            print("¡Acierto!")
            aciertos += 1
        else:
            print("Agua.")
            fallos += 1

        if aciertos == CANTIDAD_BARCOS:
            print("¡Ganaste! Hundiste todos los barcos.")
            break

    print("\n🔚 Juego terminado.")
    mostrar_tablero(tablero, disparos)
    print(f"Aciertos: {aciertos}")
    print(f"Fallos: {fallos}")
    print("Barcos que quedaron en pie (X = hundido, B = sobrevivió):")

    # Mostrar tablero final con barcos sobrevivientes
    for i in range(N):
        fila = ""
        for j in range(N):
            if tablero[i][j] and disparos[i][j]:
                fila += "X "
            elif tablero[i][j]:
                fila += "B "
            elif disparos[i][j]:
                fila += "O "
            else:
                fila += ". "
        print(fila)


if __name__ == "__main__":
    jugar()
