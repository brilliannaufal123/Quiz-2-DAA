# Quiz-2-DAA
run python main.py

Controls:
arrow keys = move
R = restart
Q = quit

DAA Quiz 2 Report
Maze Explorer
Fawwaz Reynardio Ednansyah | 5025241167 
Naufal Bintang Brillian | 5025241168

1. Design
In this case, we designed a maze explorer game that combines a procedurally generated maze with an algorithmic challenge. The core idea is to require players to navigate through a maze more efficiently than a DFS algorithm that serves as the benchmark.
Project Structure: We organized the code into three main files. The config.py file contains all the constants, logic.py contains the game logic and algorithms, and ui.py handles all the rendering. This separation keeps the code clean and easy to maintain.
Visual Style: The maze is displayed as a simple 2D grid from a top-down perspective. We kept the visual design minimal and straightforward, focusing on making the cells clear and responsive to player movement.
Level Difficulty: The difficulty scales mathematically as the player progresses. When a player clears a level, the grid size increases, making the next maze larger and more complex. If the player fails, they go back to level 1 with a smaller grid. This approach creates natural difficulty progression without manual configuration.
Win and Lose Conditions: The most important design choice is how we define success. A player wins a level only if the number of steps taken is less than or equal to the DFS distance. If the player uses more steps than DFS, they lose and must restart from level 1. This forces players to think strategically about their route instead of just wandering around.

2. Implementation
The game is built entirely in Python using Pygame for display and input handling.
Maze Generation: The maze is generated using a stack-based recursive backtracker algorithm. The algorithm starts from one cell and carves paths through walls into unvisited neighboring cells. After the main path is complete, we randomly remove additional walls to create loops and multiple routes through the maze. This makes the pathfinding challenge more difficult since there is no single obvious path.
Pathfinding Algorithm: The dfs_solve function implements a Depth-First Search algorithm using a stack and a dictionary to track visited cells. The function returns the minimum number of steps needed to reach the exit. This value becomes the benchmark against which we measure the player's performance.
Game State Management: The Game class handles all the core game state, including the player's current position, the history of movements (shown as a trail on screen), and the calculation of grid dimensions based on the current level.
Rendering and Input: The ui.py module converts grid coordinates to screen pixels and renders everything the player sees. Keyboard input is mapped to movement directions through a KEY_DIRECTIONS dictionary. The player's trail is rendered using pygame.Surface with alpha blending to create a transparent effect.

3. Evaluation
The game evaluates player performance through a direct comparison between the player's path and the DFS path.
Performance Metric: The primary metric is the number of steps taken by the player compared to the DFS distance.
Win Condition: A level is successfully cleared only if:
Steps_Taken ≤ DFS_Distance
This condition forces players to minimize backtracking and find an efficient route.
Failure Penalty: If the player uses more steps than the DFS algorithm, they fail the level and restart from level 1 with a smaller grid. There is no second chance.
Visual Feedback: After each level ends, a result card appears showing both the player's steps and the DFS steps side by side. The DFS path is also visualized on the maze as dots, allowing players to see the optimal route they should have followed.

4. Conclusion
Maze Explorer successfully brings together a fundamental computer science algorithm and an engaging gameplay mechanic. By making the win condition depend on path efficiency rather than simply reaching the exit, the game encourages strategic thinking and careful route planning. The code is well-organized with clear separation between game logic and rendering, and the difficulty scaling system naturally increases the challenge as players progress.

Contribution Statement
This project was completed by a two-person team with the following contribution breakdown:
Fawwaz (50%): Conceived the game idea, designed the overall gameplay mechanics, and implemented the DFS algorithm for maze generation and pathfinding.
Bintang (50%): Created the user interface and all visual elements of the game, and contributed to writing the final report.


