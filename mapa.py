# Autor: Adrià Sánchez Calvo
# https://github.com/Ninjakito
# https://sanchezcalvo.com

import random

class CelulaVacia():
    def estaViva(self) -> bool:
        return False

class Celula():
    def __init__(self, estado: bool = False) -> None:
        self.viva = estado

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
    
    def revivir(self) -> None:
        self.viva = True

    def __repr__(self) -> str:
        if self.viva: return "'O'"
        else: return "' '"

class Juego():
    def __init__(self, columnas: int = 10, filas: int = 10) -> None:
        self.columnas = columnas
        self.filas = filas
        self.tablero = self.crearTablero()
    
    def crearTablero(self) -> list:
        tablero = []
        for fila in range(self.filas):
            tablero.append([])
            for columna in range(self.columnas):
                viva = random.choices([True, False])
                tablero[fila].append(Celula(viva[0]))
        return tablero
