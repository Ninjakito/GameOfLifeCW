# Autor: Adrià Sánchez Calvo
# https://github.com/Ninjakito
# https://sanchezcalvo.com

import os
import pygame
from mapa import Juego, Celula, CelulaVacia

juego = columnas = filas = None

ANCHOVENTANA = 1280
ALTOVENTANA = 720

LIMITEFPS = 165

COLOREDICION = (56, 107, 69)
COLORNEGRO = (0, 0, 0)

def numeroUsuario(pregunta: str) -> int:
    while True:
        try:
            respuesta = input(pregunta)
            respuestaint = int(respuesta)
            if respuestaint < 0: raise ValueError
            return respuestaint
        except ValueError:
            print(f"'{respuesta}' no es un numero, ha de ser un numero entero positivo")

def assignarCelulasRededor(tablero: list) -> None:
    # Por cada fila
    for fila in range(len(tablero)):
        # Por cada columna
        for columna in range(len(tablero[fila])):
            celulas = []
            # Mira las filas -1, 0, 1 en relativo a la celula que estamos mirando
            for i in range(-1, 2):
                # Mira las columas -1, 0, 1 en relativo a la celula que estamos mirando
                for j in range(-1, 2):
                    try:
                        # Eso quiere decir que es la celula que estamos comprobando, asi que dejamos ese slot vacio
                        nuevafila = fila + i
                        nuevacolumna = columna + j
                        # En caso de que intente cojer celulas de la parte de arriba de la tabla o de la izquierda
                        if nuevacolumna < 0 or nuevafila < 0: raise IndexError
                        if nuevafila == fila and nuevacolumna == columna: 
                            celulas.append([CelulaVacia()])
                            continue
                        celulas.append([tablero[nuevafila][nuevacolumna]])
                    except IndexError:
                        # Es decir, que no hay mapa, asi que lo dejamos vacio
                        celulas.append([CelulaVacia()])
            tablero[fila][columna].celulasAdyacentes(celulas)

def getCelulasVivas(tablero: list) -> list:
    return [celula for fila in tablero for celula in fila if celula.estaViva()]

def logicaVida(tablero: list) -> None:
    celulasvivas = getCelulasVivas(tablero)
    funcionescelulas = []
    for celula in celulasvivas:
        # Aqui la celula esta viva 100%
        celula: Celula
        cantidadVivas = len(getCelulasVivas(celula.getCelulasRededor()))
        if (not cantidadVivas == 2) and (not cantidadVivas == 3):
            funcionescelulas.append(celula.matar)

        for celularededorlist in celula.getCelulasRededor():
            # Aqui la celula no sabemos si esta viva o muerta
            celularededor = celularededorlist[0]
            if type(celularededor) is CelulaVacia: continue
            
            celularededor: Celula
            cantidadVivas = len(getCelulasVivas(celularededor.getCelulasRededor()))
            if celularededor.estaViva():
                if (not cantidadVivas == 2) and (not cantidadVivas == 3):
                    funcionescelulas.append(celularededor.matar)
            else:
                if cantidadVivas == 3:
                    funcionescelulas.append(celularededor.revivir)
    # Esto se hace de esta manera, porque si no, las celulas mueren antes de que las
    # otras celulas comprueben si las de alrededor estan vivas 
    for funcioncelula in funcionescelulas:
        funcioncelula()

def main() -> None:
    pygame.init()

    columnas = numeroUsuario("Cuantas columnas quieres? ")
    filas = numeroUsuario("Cuantas filas quieres? ")
    juego = Juego(columnas=columnas, filas=filas)
    salir = start = False

    ventana = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption('El juego de la vida')

    grupoSprites = pygame.sprite.Group()

    reloj = pygame.time.Clock()

    juego.crearTablero(ANCHOVENTANA, ALTOVENTANA)

    assignarCelulasRededor(juego.tablero)

    escalax = ANCHOVENTANA /columnas
    escalay = ALTOVENTANA / filas

    # grupoSprites.add([celula for fila in juego.tablero for celula in fila])
    # grupoSprites.draw(ventana)

    ventana.fill(COLOREDICION)

    while not salir:
        # Input del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                break
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (not start):
                # Obtener la posición del ratón y calcular la celda correspondiente
                x, y = pygame.mouse.get_pos()
                fila = int(y // escalay)
                columna = int(x // escalax)
                # Cambiar el estado de la celda
                if juego.tablero[fila][columna].estaViva():
                    juego.tablero[fila][columna].matar()
                else:
                    juego.tablero[fila][columna].revivir()
                juego.tablero[fila][columna].dibujar(ventana)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True if not start else False
                    grupoSprites.empty()
                    grupoSprites.add(getCelulasVivas(juego.tablero))

                    ventana.fill(COLOREDICION if not start else COLORNEGRO)

                    grupoSprites.draw(ventana)

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_ESCAPE]:
            salir = True
            break

        # Input del jugador

        deltatime = reloj.tick(LIMITEFPS)

        if start:
            logicaVida(juego.tablero)

            grupoSprites.empty()
            grupoSprites.add(getCelulasVivas(juego.tablero))

            ventana.fill(COLORNEGRO)

            grupoSprites.draw(ventana)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    try:    
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print(f"{'¡Adios!':~^20}")