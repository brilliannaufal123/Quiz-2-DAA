import random
import time
from config import DIRS, get_level_dims, WIN_W, WIN_H

# Check if a cell is walkable
def can_walk(maze, x, y, col, rows):
    if x < 0 or x >= col or y < 0 or y >= rows:
        return False
    if maze[y][x] == True:
        return False     
    return True

# do the maze using DFS returns the path and length 
def dfs_solve(maze, start, end, col, rows):
    stack = [start]
    visited = {start: None}

    while len(stack) > 0:
        cell = stack.pop()
        if cell == end:
            break

        random_dir = list(DIRS)
        random.shuffle(random_dir)

        for dir_x, dir_y in random_dir:
            next_x = cell[0] + dir_x
            next_y = cell[1] + dir_y
            next_cell = (next_x, next_y)

            if can_walk(maze, next_x, next_y, col, rows):
                if next_cell not in visited:
                    visited[next_cell] = cell
                    stack.append(next_cell)

    # If end never reached, return empty
    if end not in visited:
        return [], 0

    # go back the path from end to start then reverse it
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = visited[current_node]
    
    path.reverse()

    distance = len(path) - 1
    return path, distance

# generate a maze and add more hole so it not linear
def build_maze(width, height, holes=20):
    # Fill walls
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(True)
        maze.append(row)

    # Start making from cell (1,1)
    maze[1][1] = False
    stack = [(1, 1)]

    while len(stack) > 0:
        current_cell = stack[-1]
        x = current_cell[0]
        y = current_cell[1]

        # Look for unvisited neighbors two steps
        possible_neighbors = []
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        
        for direction_x, direction_y in directions:
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y

            if 1 <= neighbor_x < width - 1 and 1 <= neighbor_y < height - 1:
                if maze[neighbor_y][neighbor_x] == True:
                    possible_neighbors.append((neighbor_x, neighbor_y, direction_x, direction_y))

        if len(possible_neighbors) > 0:
            # getrandom neighbor and make path
            neighbor_x, neighbor_y, direction_x, direction_y = random.choice(possible_neighbors)

            between_x = x + (direction_x // 2)
            between_y = y + (direction_y // 2)
            maze[between_y][between_x] = False  #Remove the wall in between

            maze[neighbor_y][neighbor_x] = False  # Mark neighbor visited
            
            stack.append((neighbor_x, neighbor_y))
        else:
            # if dead end then backtrack
            stack.pop()

    # make exit area open
    maze[height- 2][width- 2] = False
    maze[height- 2][width- 3] = False

    # remove extra walls randomly
    for _ in range(holes):
        random_x = random.randint(1, width-2)
        random_y = random.randint(1, height-2)
        maze[random_y][random_x] = False
        
    return maze

# game class
class Game:
    def __init__(self):
        self.level = 1
        self.reset()

    # --- Re-initialize everything for the current level ---
    def reset(self):
        self.col, self.rows, self.cell = get_level_dims(self.level)

        # make maze center
        maze_width_pixels = self.col * self.cell
        maze_height_pixels = self.rows * self.cell
        self.offset_x = int((WIN_W - maze_width_pixels) / 2)
        self.offset_y = int((WIN_H - maze_height_pixels) / 2)

        # Build maze and get start and end points
        self.maze = build_maze(self.col, self.rows)
        self.start = (1, 1)
        self.end = (self.col - 2, self.rows - 2)

        # solve the maze to know the best distance
        self.dfs_path, self.dfs_dist = dfs_solve(self.maze, self.start, self.end, self.col, self.rows)

        # Reset player position and tracking variables
        self.player_x = self.start[0]
        self.player_y = self.start[1]
        self.trail = [self.start]
        self.steps_taken = 0

        # Reset game state and timer
        self.is_game_over = False
        self.game_result = ""
        self.start_time = time.time()
        self.end_time = None

    # go to the next level on win if lose restart from level 1
    def next_level(self):
        if self.game_result == "WIN":
            self.level += 1
        else:
            self.level = 1
        self.reset()

    # move plater and add trail
    def move_player(self, direction):
        if self.is_game_over:
            return 
            
        dir_x = direction[0]
        dir_y = direction[1]
        next_x = self.player_x + dir_x
        next_y = self.player_y + dir_y

        if not can_walk(self.maze, next_x, next_y, self.col, self.rows):
            return

        next_position = (next_x, next_y)

        # count a step if visiting a new cell
        if next_position not in self.trail:
            self.steps_taken += 1
            self.trail.append(next_position)

        self.player_x = next_x
        self.player_y = next_y

        # Check if player in the exit
        if next_position == self.end:
            self.is_game_over = True
            self.end_time = time.time()

            # Win if steps taken better than DFS
            if self.steps_taken <= self.dfs_dist:
                self.game_result = "WIN"
            else:
                self.game_result = "LOSE"

    # get time
    def get_time(self):
        if self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return time.time() - self.start_time