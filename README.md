# Game of Life (Juego de la Vida)

## English
This project is a Python implementation of John Horton Conway's Game of Life. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

### Game rules
There are 2 types of cells:

#### Cell "X", alive
A cell is alive if it has 2 or 3 living cells around it, neither more nor less, diagonals included, if it has more or less, it dies.

#### Cell " ", dead
A cell revives if it has exactly 3 living cells around it, otherwise it remains dead.

### Installation
1. Clone this repository
2. Install the requirements with `pip install -r requirements.txt`
3. Run `python main.py`

### Usage
You can modify the initial state in `main.py` to see how different patterns evolve over time.

## Español
Este proyecto es una implementación en Python del Juego de la Vida de John Horton Conway. El Juego de la Vida es un autómata celular ideado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, lo que significa que su evolución está determinada por su estado inicial, sin necesidad de más entradas.

### Reglas del juego
Hay 2 tipos de celulas:

#### Celula "O", viva
Una celula esta viva si tiene 2 o 3 al rededor vivas, ni mas ni menos, diagonales incluidas, si tiene más o menos, muere

#### Celula " ", muerta
Una celula revive si tiene exactamente 3 celulas a su alrededor vivas, en caso contrario, sigue muerta

### Instalación
1. Clona este repositorio
2. Instala los requisitos con `pip install -r requirements.txt`
3. Ejecuta `python main.py`

### Uso
Puedes modificar el estado inicial en `main.py` para ver cómo evolucionan diferentes patrones con el tiempo.