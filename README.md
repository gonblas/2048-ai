# 2048 AI

![Python Version](https://img.shields.io/badge/python-3.11.5-blue.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Project Status](https://img.shields.io/badge/status-finished-brightgreen.svg)

[English](https://github.com/gonblas/2048-ai/blob/main/README.md) | [Español](https://github.com/gonblas/2048-ai/blob/main/README_es.md)

# Game Description

**[2048](https://en.wikipedia.org/wiki/2048_(video_game))** is a captivating puzzle game where the main goal is to combine numbered blocks to reach the coveted 2048 tile. The board is presented as a grid, and the central game mechanic involves merging blocks.

## How to Play

**Basic Instructions:**
- Use the keyboard arrows (up, down, left, right) to move tiles on the grid.
- When two tiles with the same number collide, they merge into a single tile with the sum value.

**Additional Details:**
- **Board Size:** The game allows customization of the board size, offering options like 3x3, 4x4, 5x5, 6x6, and 8x8. Each size has its corresponding name.
  - 3x3: Tiny
  - 4x4: Classic
  - 5x5: Big
  - 6x6: Bigger
  - 8x8: Huge

- **Loss Condition:** The game ends when no possible moves allow merging blocks.

**Game Modes:**
- **User Mode:** Experience the challenge and fun of the game by taking direct control and applying your strategic skills.
- **AI Mode:** Delegate the challenge to an advanced artificial intelligence. Watch how the algorithm seeks the best block combinations and plans efficient moves. You can press the space bar to pause the AI.

## Artificial Intelligence

### Monte Carlo Tree Search

#### Description

[Monte Carlo Tree Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) (MCTS) is a heuristic search algorithm used in decision-making processes, especially in software designed for playing board games. In the context of games like 2048, MCTS is employed to solve the game tree.

The primary focus of MCTS lies in analyzing the most promising moves, expanding the search tree by randomly sampling the search space. In each simulation, the game is played out to the end by randomly selecting moves. The final outcome of each simulation is used to weigh the nodes in the game tree, so better nodes are more likely to be chosen in future simulations.

![mcts_diagram](assets/mcts_diagram.svg)

Each round of Monte Carlo Tree Search consists of four steps:

#### How It's Applied in the 2048 Game

1. **Selection:** It starts at the root node (current game state) and recursively selects descendant nodes based on a selection strategy.

2. **Expansion:** If the selected node does not represent a final game state, it expands by generating nodes corresponding to possible moves from that state.

3. **Simulation:** Complete games are simulated from the newly created nodes (or already existing nodes) to a terminal state, using random or heuristic strategies.

4. **Backpropagation:** The result information from the simulation is propagated upward through the tree, updating the statistics of visited nodes.

5. **Move Selection:** Finally, the move that leads to the most promising child node is chosen based on the statistics collected during the simulations.

### Expectiminimax Algorithm

The [Expectiminimax Algorithm](https://en.wikipedia.org/wiki/Expectiminimax) is an extension of the minimax algorithm designed to handle nodes of probability in games or problems with uncertainty. It is used in situations where future events are uncertain and all possibilities must be considered, weighted by their probability. In 2048, there is randomness in the tile number (90% chance of getting a 2, and 10% chance of getting a 4) and its position (which is randomly chosen from all empty positions).

To control the complexity of the algorithm, the concept of "depth" is introduced. The depth of the search tree determines how far possible sequences of moves will be explored. A higher depth value implies more thorough exploration but at the expense of higher computational cost.

![expectiminimax](assets/expectiminimax_diagram.svg)

#### How It's Applied in the 2048 Game

1. **Game Tree Generation:** A tree representing all possible sequences of moves and game states, including the probabilities of generating new blocks, is built.

2. **Position Evaluation:** Terminal game positions are evaluated, and utility values are assigned to each state, considering the score and other relevant factors.

   - Number of Open Tiles: The number of open tiles is considered, influencing the score.

   - **Bonus for Large Values Following the Shape of a Snake:** A bonus is awarded for large values located on the edges of the board.

   - Penalty for Lack of Monotonicity in Rows and Columns: There is a penalty for lack of monotonicity in rows and columns.

   - Bonus for the Number of Potential Merges: A bonus is awarded for the number of potential merges.
   
   Only what's in bold actually affects the final heuristic value of each move.

3. **Probability Propagation:** In probability nodes (where new blocks are generated), the probability of generating each block is taken into account, and the expected value is weighted.

4. **Move Choice:** The move that maximizes (or minimizes, depending on the turn) the expected value is chosen, considering all possible sequences of moves and their probabilities.

## How to Run the Code

### Prerequisites

Before using this repository, make sure to meet the following requirements:

- Have [Python](https://www.python.org/) installed on your system. Python **3.11.5** was used.
- Have the `virtualenv` tool installed (you can install it by running `pip install virtualenv`).

### Execution Steps

1. Clone the repository to your local machine and navigate to the folder.
   ```bash
    git clone https://github.com/gonblas/2048-ai.git

    cd 2048-ai
   ```

2. Create a virtual environment with Python.
   ```bash
    python -m venv venv
   ```
3. Activate the virtual environment.
   ```bash
    ## On Windows:
   .\venv\Scripts\activate

   ## On Linux/macOS:
   source venv/bin/activate
   ```
4. Install the dependencies.
   ```bash
    pip install -r requirements.txt
   ```
5. Run the [main.py](https://github.com/gonblas/2048-ai/blob/main/src/main.py) file.
    ```bash
    python src/main.py
   ```

___

Feel free to modify or expand the content according to your preferences. This README provides a detailed overview of your project, making it more informative and user-friendly.



