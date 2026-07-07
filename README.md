# Pixel Maze Explorer
### Design & Analysis of Algorithm Quiz 2 Report

| Name | ID |
|-----|--------|
| **Fawwaz Reynardio Ednansyah** | 5025241167 |
| **Naufal Bintang Brillian** | 5025241168 |

---

## How to Run

```
python main.py
```

**Controls**

| Key | Action |
|-----|--------|
| Arrow keys | Move |
| R | Restart |
| Q | Quit |

---

## 1. Design

This project presents a maze explorer game that combines a procedurally generated maze with an algorithmic performance challenge. The central design principle requires players to navigate the maze at least as efficiently as a Depth-First Search (DFS) algorithm, which serves as the performance benchmark.

**Project Structure.** The codebase is organized into three primary modules to maintain clarity and separation of concerns: `config.py` stores all constants, `logic.py` implements the game logic and algorithms, and `ui.py` manages rendering. This modular structure keeps the implementation maintainable and easy to extend.

**Visual Style.** The maze is rendered as a simple two-dimensional grid viewed from a top-down perspective. The visual design was kept minimal and clean, with an emphasis on cell clarity and responsive player movement.

**Level Difficulty.** Difficulty scales mathematically as the player progresses. Upon successfully clearing a level, the grid size increases, producing a larger and more complex maze. Upon failure, the player is returned to level 1 with a smaller grid. This mechanism produces a natural difficulty curve without requiring manual level configuration.

**Win and Lose Conditions.** The defining design decision is how success is determined. A player wins a level only if the number of steps taken is less than or equal to the DFS-computed shortest distance. If the player exceeds this step count, the level is failed and the player must restart from level 1. This condition compels players to plan their route strategically rather than exploring the maze arbitrarily.

## 2. Implementation

The game is implemented entirely in Python, using Pygame for rendering and input handling.

**Maze Generation.** The maze is generated using a stack-based recursive backtracker algorithm. Beginning from an initial cell, the algorithm carves paths by breaking walls into unvisited neighboring cells. Once the primary path structure is complete, additional walls are removed at random to introduce loops and alternative routes, increasing the difficulty of the pathfinding challenge by eliminating any single obvious solution.

**Pathfinding Algorithm.** The `dfs_solve` function implements a Depth-First Search using a stack combined with a dictionary to track visited cells. The function returns the minimum number of steps required to reach the exit, which serves as the benchmark against which player performance is evaluated.

**Game State Management.** The `Game` class manages all core game state, including the player's current position, the movement history rendered as an on-screen trail, and the grid dimensions computed for the current level.

**Rendering and Input.** The `ui.py` module handles conversion of grid coordinates into screen pixel coordinates and renders all visual elements. Keyboard input is mapped to movement directions via a `KEY_DIRECTIONS` dictionary. The player's trail is rendered using a `pygame.Surface` with alpha blending to produce a transparency effect.

## 3. Evaluation

Player performance is evaluated through a direct comparison between the player's path length and the DFS-computed path length.

**Performance Metric.** The primary evaluation metric is the number of steps taken by the player relative to the DFS distance.

**Win Condition.** A level is successfully cleared if and only if:

```
Steps_Taken ≤ DFS_Distance
```

This condition compels players to minimize backtracking and identify an efficient route through the maze.

**Failure Penalty.** If the player's step count exceeds the DFS distance, the level is failed and the player restarts from level 1 with a smaller grid. No partial credit or second attempt is granted.

**Visual Feedback.** At the conclusion of each level, a result card displays the player's step count alongside the DFS step count for direct comparison. Additionally, the DFS-computed path is visualized on the maze as a series of dots, allowing the player to review the optimal route.

## 4. Conclusion

Maze Explorer successfully integrates a fundamental computer science algorithm with an engaging gameplay mechanic. By conditioning success on path efficiency rather than mere completion, the game encourages strategic thinking and deliberate route planning. The implementation maintains a clear separation between game logic and rendering, and the difficulty scaling system provides a natural and progressively increasing challenge.

---

## Contribution Statement

This project was completed by a two-person team with the following contribution breakdown:

- **Fawwaz (50%):** Conceived the game concept, designed the overall gameplay mechanics, and implemented the DFS algorithm for maze generation and pathfinding.
- **Bintang (50%):** Designed and implemented the user interface and all visual elements of the game, and contributed to writing the final report.
