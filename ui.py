import pygame
import sys
from config import WIN_W, WIN_H, FPS, COLORS

pygame.init()
screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Maze Explorer")
clock = pygame.time.Clock()

BIGFONT = pygame.font.SysFont("arial", 42, bold=True)
MEDIUMFONT = pygame.font.SysFont("arial", 24, bold=True)
SMALLFONT = pygame.font.SysFont("arial", 18)

KEY_DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

WALL_IMG = pygame.image.load("wall.png").convert_alpha()
FLOOR_IMG = pygame.image.load("floor.png").convert_alpha()

def draw_maze(game):
    wall_texture = pygame.transform.scale(WALL_IMG, (game.cell, game.cell))
    floor_texture = pygame.transform.scale(FLOOR_IMG, (game.cell, game.cell))
    for y in range(game.rows):
        for x in range(game.col):
            is_wall = game.maze[y][x]

            screen_x = game.offset_x + (x * game.cell)
            screen_y = game.offset_y + (y * game.cell)
            cell_rect = pygame.Rect(screen_x, screen_y, game.cell, game.cell)
            
            if is_wall == True:
                screen.blit(wall_texture, cell_rect)
            else:
                screen.blit(floor_texture, cell_rect)
                pygame.draw.rect(screen, COLORS["grid_lines"], cell_rect, 1)

    for position in game.trail:
        trail_x = game.offset_x + (position[0] * game.cell)
        trail_y = game.offset_y + (position[1] * game.cell)

        trail_surface = pygame.Surface((game.cell, game.cell), pygame.SRCALPHA)
        trail_surface.fill((COLORS["trail"][0], COLORS["trail"][1], COLORS["trail"][2], 255))
        screen.blit(trail_surface, (trail_x, trail_y))

    if game.is_game_over:
        for position in game.dfs_path:
            center_x = game.offset_x + (position[0] * game.cell) + (game.cell // 2)
            center_y = game.offset_y + (position[1] * game.cell) + (game.cell // 2)
            
            dot_size = game.cell // 6
            if dot_size < 2:
                dot_size = 2
                
            pygame.draw.circle(screen, COLORS["dfs_path"], (center_x, center_y), dot_size)

    start_x = game.offset_x + (game.start[0] * game.cell)
    start_y = game.offset_y + (game.start[1] * game.cell)
    pygame.draw.rect(screen, COLORS["green_color"], (start_x, start_y, game.cell, game.cell))

    end_x = game.offset_x + (game.end[0] * game.cell)
    end_y = game.offset_y + (game.end[1] * game.cell)
    pygame.draw.rect(screen, COLORS["end_point"], (end_x, end_y, game.cell, game.cell))

    p_screen_x = game.offset_x + (game.player_x * game.cell)
    p_screen_y = game.offset_y + (game.player_y * game.cell)
    player_rect = pygame.Rect(p_screen_x, p_screen_y, game.cell, game.cell)

    corner_radius = game.cell // 4
    pygame.draw.rect(screen, COLORS["player"], player_rect, border_radius=corner_radius)


def draw_hud(game):
    level_text = MEDIUMFONT.render(f"LEVEL {game.level}", True, COLORS["text_main"])
    steps_text = MEDIUMFONT.render(f"Steps: {game.steps_taken}", True, COLORS["text_main"])

    time = game.get_time()
    time_text = MEDIUMFONT.render(f"Time: {time:0.1f}s", True, COLORS["text_main"])
    
    screen.blit(level_text, (20, 20))
    screen.blit(steps_text, (20, 50))
    screen.blit(time_text, (20, 80))


def draw_result_card(game):
    card_width = 280
    card_height = 220
    card_x = 1200
    card_y = 20

    if game.game_result == "WIN":
        border_color = COLORS["green_color"]
        title_text = "YOU WIN!"
        prompt_text = "SPACE: Next Level"
    else:
        border_color = COLORS["red_color"]
        title_text = "You Failed!"
        prompt_text = "SPACE: Retry"

    card_rect = pygame.Rect(card_x, card_y, card_width, card_height)
    pygame.draw.rect(screen, COLORS["ui_card"], card_rect)
    pygame.draw.rect(screen, border_color, card_rect, 3, border_radius=12)

    title_surface = MEDIUMFONT.render(title_text, True, border_color)
    title_x = card_x + (card_width // 2) - (title_surface.get_width() // 2)
    screen.blit(title_surface, (title_x, card_y + 30))

    card_at_end = [
        f"Your steps: {game.steps_taken}",
        f"DFS steps: {game.dfs_dist}",
    ]
    
    for index, text in enumerate(card_at_end):
        text_surface = SMALLFONT.render(text, True, COLORS["text_main"])
        text_x = card_x + (card_width // 2) - (text_surface.get_width() // 2)
        text_y = card_y + 80 + (index * 25)
        screen.blit(text_surface, (text_x, text_y))

    prompt_surface = SMALLFONT.render(prompt_text, True, COLORS["text_main"])
    prompt_x = card_x + (card_width // 2) - (prompt_surface.get_width() // 2)
    screen.blit(prompt_surface, (prompt_x, card_y + card_height - 30))


def run(game):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if game.is_game_over == False:
                    if event.key in KEY_DIRECTIONS:
                        chosen_direction = KEY_DIRECTIONS[event.key]
                        game.move_player(chosen_direction)

                if game.is_game_over == True:
                    if event.key == pygame.K_SPACE:
                        game.next_level()

                if event.key == pygame.K_r:
                    game.reset()

        screen.fill(COLORS["background"])
        
        draw_maze(game)
        draw_hud(game)
        
        if game.is_game_over == True:
            draw_result_card(game)

        pygame.display.flip()
        clock.tick(FPS)