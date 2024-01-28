User
# 2048 AI

# Descripción del Juego

El **[2048](https://en.wikipedia.org/wiki/2048_(video_game))** es un fascinante juego de rompecabezas en el que el objetivo principal es combinar bloques numerados para alcanzar la codiciada casilla 2048. El tablero se presenta como una cuadrícula, y la mecánica central del juego es la combinación de bloques.

## Cómo Se Juega

**Instrucciones Básicas:**
- Utiliza las flechas del teclado (arriba, abajo, izquierda, derecha) para mover las casillas en la cuadrícula.
- Cuando dos casillas con el mismo número colisionan, se fusionan en una única casilla con el valor de la suma.

**Detalles Adicionales:**
- **Tamaño del Tablero:** El juego permite la personalización del tamaño del tablero, ofreciendo opciones como 3x3, 4x4, 5x5, 6x6 y 8x8. Cada tamaño tiene su propio nombre correspondiente.
  - 3x3: Tiny
  - 4x4: Classic
  - 5x5: Big
  - 6x6: Bigger
  - 8x8: Huge

- **Condición de derrota:** El juego finaliza cuando no hay movimientos posibles que permitan combinar bloques.

**Modos de Juego:**
- **Modo Usuario:** Experimenta el desafío y la diversión del juego tomando el control directo y aplicando tus habilidades de estrategia.
- **Modo AI:** Delega el desafío a una inteligencia artificial avanzada. Observa cómo el algoritmo busca la mejor combinación de bloques y planifica movimientos eficientes. Puedes presionar la barra espaciadora para parar a la IA.

## Inteligencia Artificial

### Monte Carlo Tree Search

#### Descripción

La [búsqueda de árboles Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) (MCTS) es un algoritmo de búsqueda heurística utilizado en procesos de toma de decisiones, especialmente en software diseñado para jugar juegos de mesa. En el contexto de juegos como el 2048, MCTS se emplea para resolver el árbol de juego.

El enfoque principal de MCTS radica en analizar los movimientos más prometedores, expandiendo el árbol de búsqueda mediante el muestreo aleatorio del espacio de búsqueda. En cada simulación, el juego se lleva a cabo hasta el final seleccionando movimientos al azar. El resultado final de cada simulación se utiliza para ponderar los nodos en el árbol de juego, de modo que los nodos mejores tienen más probabilidades de ser elegidos en simulaciones futuras.

![mcts_diagram](assets/mcts_diagram.svg)


Cada ronda de búsqueda de árboles Monte Carlo consta de cuatro pasos:


#### Cómo se Aplica en el Juego 2048

1. **Selección:** Comienza en el nodo raíz (estado actual del juego) y selecciona recursivamente nodos descendientes basándose en una estrategia de selección.

2. **Expansión:** Si el nodo seleccionado no representa un estado final del juego, se expande generando los nodos correspondientes a los posibles movimientos desde ese estado.

3. **Simulación:** Se simulan juegos completos desde los nodos recién creados (o nodos ya existentes) hasta un estado terminal, utilizando estrategias aleatorias o heurísticas.

4. **Retropropagación:** La información del resultado de la simulación se propaga hacia arriba a través del árbol, actualizando las estadísticas de los nodos visitados.

5. **Selección de Jugada:** Finalmente, se elige la jugada que lleva al nodo hijo más prometedor basándose en las estadísticas recopiladas durante las simulaciones.

### Algoritmo Expectiminimax

El [Algoritmo Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax) es una extensión del algoritmo minimax, diseñado para manejar nodos de probabilidad en juegos o problemas con incertidumbre. Se utiliza en situaciones donde los eventos futuros son inciertos y se deben considerar todas las posibilidades ponderadas por su probabilidad. En el 2048, existe una aleatoriedad en el numero ficha que sale (90% de posibilidad de que salga el 2, y 10% de que salga el 4) y su posicion (la cual es una aleatoria entre todas las que se encuentran vacias).

Para controlar la complejidad del algoritmo, se introduce el concepto de "depth". La profundidad del árbol de búsqueda determina hasta qué punto se explorarán las posibles secuencias de movimientos. Un mayor valor de profundidad implica una exploración más exhaustiva pero a expensas de un mayor costo computacional.

![expectiminimax](assets/expectiminimax_diagram.svg)



#### Cómo se Aplica en el Juego 2048s

1. **Generación del Árbol de Juego:** Se construye un árbol que representa todas las posibles secuencias de movimientos y estados del juego, incluyendo las probabilidades de generación de nuevos bloques.

2. **Evaluación de Posiciones:** Se evalúan las posiciones terminales del juego y se asignan valores de utilidad a cada estado, considerando la puntuación y otros factores relevantes.

    - Número de Casillas Abiertas: Se considera la cantidad de casillas abiertas, influyendo en la puntuación.

    - **Bonificación por Grandes Valores Siguiendo La Forma de un Snake:** Se otorga una bonificación por grandes valores ubicados en los bordes del tablero.

    - Penalización por Falta de Monotonía en Filas y Columnas: Existe una penalización por falta de monotonía en filas y columnas.

    - Bonificación por Cantidad de Fusiones Potenciales: Se otorga una bonificación por la cantidad de fusiones potenciales.
  
  Solo aquello en negrita es lo que realmente afecta al valor heuristico final de cada movimiento.

3. **Propagación de Probabilidades:** En los nodos de probabilidad (donde se generan nuevos bloques), se toma en cuenta la probabilidad de generación de cada bloque y se pondera el valor esperado.

4. **Elección de Jugada:** Se elige la jugada que maximiza (o minimiza, según el turno) el valor esperado, considerando todas las posibles secuencias de movimientos y sus probabilidades.




## Cómo Ejecutar el Código

### Requisitos previos

Antes de utilizar este repositorio, asegúrate de cumplir con los siguientes requisitos:

- Tener [Python](https://www.python.org/) instalado en tu sistema. Se utilizo python **3.11.5**.
- Contar con la herramienta `virtualenv` instalada (puedes instalarla ejecutando `pip install virtualenv`).


### Pasos para la ejecución

1. Clona el repositorio a tu máquina local e ingresa en la carpeta.
   ```bash
    git clone https://github.com/gonblas/2048-ai.git

    cd 2048-ai
   ```

2. Crea un entorno virtual con Python.
   ```bash
    python -m venv venv
   ```
3. Activa el entorno virtual.
   ```bash
    ## En Windows:
    .\venv\Scripts\activate

    ## En Linux/macOS:
    source venv/bin/activate
   ```
4. Instala las dependencias.
   ```bash
    pip install -r requirements.txt
   ```
5. Ejecuta el archivo [main.py](https://github.com/gonblas/2048-ai/blob/main/src/main.py).
    ```bash
    python src/main.py
   ```


