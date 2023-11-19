# Autor: Adrià Sánchez Calvo
# https://github.com/Ninjakito
# https://sanchezcalvo.com

import random
import pygame

class Cuadrado(pygame.sprite.Sprite):
    def __init__(self, ancho, alto, x, y, color=(255, 255, 255)):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def cambiarColor(self, color=(255, 255, 255)):
        self.image.fill(color)

class CelulaVacia():
    def estaViva(self) -> bool:
        return False

class Celula(Cuadrado):
    def __init__(self, ancho: int, alto: int, x: int, y: int, viva: bool = False) -> None:
        super().__init__(ancho, alto, x, y)
        self.viva = viva

    def celulasAdyacentes(self, celulas: list) -> None:
        self.celulas = celulas

    def getCelulasRededor(self) -> list:
        try:
            return self.celulas
        except AttributeError:
            return [[CelulaVacia()], [CelulaVacia()], [CelulaVacia()],
                    [CelulaVacia()], [CelulaVacia()], [CelulaVacia()], 
                    [CelulaVacia()], [CelulaVacia()], [CelulaVacia()]]

    def estaViva(self) -> bool:
        return self.viva

    def matar(self) -> None:
        self.viva = False
        self.cambiarColor((0, 0, 0))
    
    def revivir(self) -> None:
        self.viva = True
        self.cambiarColor((255, 255, 255))

    def __repr__(self) -> str:
        if self.viva: return "'O'"
        else: return "' '"

class Juego():
    def __init__(self, columnas: int = 10, filas: int = 10) -> None:
        self.columnas = columnas
        self.filas = filas
    
    def crearTablero(self, anchoventana: int = 1280, altoventana: int = 720) -> list:
        tablero = []
        x = 0
        y = 0
        escalax = anchoventana // self.columnas
        escalay = altoventana // self.filas
        for fila in range(self.filas):
            tablero.append([])
            for columna in range(self.columnas):
                viva = random.choices([True, False])
                viva = viva[0]
                tablero[fila].append(Celula(escalax, escalay, x, y, viva))
                x += escalax
            x = 0
            y += escalay
        self.tablero: list = tablero
