#--------------------------------------------------------------INSTRUCCIONES--------------------------------------------------------------------

# Juego de tres en raya (o triqui) hecho con diccionarios, para jugar se debe acceder a las keys del diccionario como las coordenadas del tablero

# Demostracion del tablero y sus coordenadas:

#    top-left |   top-mid  | top-right
#    ---------+------------+-----------
#    mid-left |   mid-mid  | mid-right
#    ---------+------------+-----------
# bottom-left | bottom-mid | bottom-right

# Ejemplo:
# Jugador X: mid-mid 

#    top-left |   top-mid  | top-right
#    ---------+------------+-----------
#    mid-left |      X     | mid-right
#    ---------+------------+-----------
# bottom-left | bottom-mid | bottom-right

#--------------------------------------------------------------INSTRUCCIONES--------------------------------------------------------------------

from os import system
import sys

# Constuir el tablero
board = {"top-left": "   ", "top-mid": "   ", "top-right": "   ",
        "mid-left": "   ", "mid-mid": "   ", "mid-right": "   ",
        "bottom-left": "   ", "bottom-mid": "   ", "bottom-right": "   "}

# Turno del jugador
turn = " X "

# Variable booleana para verificar si hay un ganador
winner = False

# Imprime el tablero con estética en consola
def printBoard(board):
    print(board["top-left"] + "|" + board["top-mid"] + "|" + board["top-right"])
    print("---+---+---")
    print(board["mid-left"] + "|" + board["mid-mid"] + "|" + board["mid-right"])
    print("---+---+---")
    print(board["bottom-left"] + "|" + board["bottom-mid"] + "|" + board["bottom-right"])

# Verifica si un jugador ha ganado, haciendo tres en raya en cualquiera de las combinaciones posibles. Retorna 'winner' como true.
def verifyWinner(board):
    global winner
    # Verificar ganador

    # Horizontales jugador X
    if((board["top-left"] == ' X ' and board["top-mid"] == ' X ' and board["top-right"] == ' X ') or
    (board["mid-left"] == ' X ' and board["mid-mid"] == ' X ' and board["mid-right"] == ' X ') or
    (board["bottom-left"] == ' X ' and board["bottom-mid"] == ' X ' and board["bottom-right"] == ' X ') or
    # Verticales jugador X
    (board["top-left"] == ' X ' and board["mid-left"] == ' X ' and board["bottom-left"] == ' X ') or
    (board["top-mid"] == ' X ' and board["mid-mid"] == ' X ' and board["bottom-mid"] == ' X ') or
    (board["top-right"] == ' X ' and board["mid-right"] == ' X ' and board["bottom-right"] == ' X ') or
    # Diagonales jugador X
    (board["top-left"] == ' X ' and board["mid-mid"] == ' X ' and board["bottom-right"] == ' X ') or
    (board["top-right"] == ' X ' and board["mid-mid"] == ' X ' and board["bottom-left"] == ' X ')):
        system("cls")
        printBoard(board)
        print("El jugador " + turn + " es el ganador")
        winner = True

    # Horizontales jugador O
    if((board["top-left"] == ' O ' and board["top-mid"] == ' O ' and board["top-right"] == ' O ') or
    (board["mid-left"] == ' O ' and board["mid-mid"] == ' O ' and board["mid-right"] == ' O ') or
    (board["bottom-left"] == ' O ' and board["bottom-mid"] == ' O ' and board["bottom-right"] == ' O ') or
    # Verticales jugador O
    (board["top-left"] == ' O ' and board["mid-left"] == ' O ' and board["bottom-left"] == ' O ') or
    (board["top-mid"] == ' O ' and board["mid-mid"] == ' O ' and board["bottom-mid"] == ' O ') or
    (board["top-right"] == ' O ' and board["mid-right"] == ' O ' and board["bottom-right"] == ' O ') or
    # Diagonales jugador O
    (board["top-left"] == ' O ' and board["mid-mid"] == ' O ' and board["bottom-right"] == ' O ') or
    (board["top-right"] == ' O ' and board["mid-mid"] == ' O ' and board["bottom-left"] == ' O ')):
        system("cls")
        printBoard(board)
        print("El jugador " + turn + " es el ganador")
        winner = True

# Ejecuta el juego
def run():
    global turn

    # Bucle while que funciona mientras no haya un ganador, cuando lo hay, se rompe el bucle
    while not winner:
        # Le pide al jugador que ingrese una coordenada para posicionar su ficha
        system("cls")
        printBoard(board)
        print("Es el turno del jugador " + turn + ". Selecciona un espacio: ")
        move = input()

        # Verificar si la casilla de la coordenada que ingresó el jugador no esta llena
        if not (board[move] == ' X ' or board[move] == ' O '):
            board[move] = turn

        # Se llama la funcion para verificar si hay un ganador despues de cada turno
        verifyWinner(board)

        # Despues del turno, si el jugador que acaba de poner su ficha es 'X' el siguiente turno es del jugador 'O'
        # En caso contrario, si el jugador que acaba de poner su ficha es 'O' el siguiente turno es del jugador 'X'
        if turn == ' X ':
            turn = ' O '
        else:
            turn = ' X '

    sys.exit(0)

# Ejecuta la funcion run() como principal
if __name__ == "__main__":
    run()