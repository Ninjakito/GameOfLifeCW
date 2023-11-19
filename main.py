# Autor: Adrià Sánchez Calvo
# https://github.com/Ninjakito
# https://sanchezcalvo.com

import os
import pygame
from mapa import Juego, Celula, CelulaVacia
from time import sleep

juego = columnas = filas = None

ANCHOVENTANA = 1280
ALTOVENTANA = 720

LIMITEFPS = 165

def Salir() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_ESCAPE]:
        return True
    return False

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

def CicloDeLaVida(tablero: list) -> pygame.sprite.Group:
    grupoSprites = pygame.sprite.Group()
    celulasvivas = getCelulasVivas(tablero)
    for celula in celulasvivas:
        # Aqui la celula esta viva 100%
        celula: Celula
        cantidadVivas = len(getCelulasVivas(celula.getCelulasRededor()))
        if (not cantidadVivas == 2) and (not cantidadVivas == 3):
            celula.matar()

        for celularededorlist in celula.getCelulasRededor():
            # Aqui la celula no sabemos si esta viva o muerta
            celularededor = celularededorlist[0]
            if type(celularededor) is CelulaVacia: continue
            
            celularededor: Celula
            cantidadVivas = len(getCelulasVivas(celularededor.getCelulasRededor()))
            if celularededor.estaViva():
                if (not cantidadVivas == 2) and (not cantidadVivas == 3):
                    celularededor.matar()
            else:
                if cantidadVivas == 3:
                    celularededor.revivir()
            grupoSprites.add(celularededor)
        grupoSprites.add(celula)
    return grupoSprites

def main() -> None:
    columnas = numeroUsuario("Cuantas columnas quieres? ")
    filas = numeroUsuario("Cuantas filas quieres? ")
    juego = Juego(columnas=columnas, filas=filas)
    salir = False

    ventana = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption('El juego de la vida')

    reloj = pygame.time.Clock()

    juego.crearTablero(ANCHOVENTANA, ALTOVENTANA)

    assignarCelulasRededor(juego.tablero)

    while not salir:
        deltatime = reloj.tick(LIMITEFPS)
        salir = Salir()
        grupoSprites = CicloDeLaVida(juego.tablero)

        ventana.fill((0, 0, 0))

        grupoSprites.draw(ventana)

        pygame.display.flip()
        print(reloj.get_fps())

if __name__ == "__main__":
    try:    
        main()
    except KeyboardInterrupt:
        print(f"{'¡Adios!':~^20}")