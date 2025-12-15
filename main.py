# Import modul yang diperlukan
import pygame, sys
from game import Game
from colors import Colors

# Inisialisasi pygame
pygame.init()

# Setup font untuk text rendering
title_font = pygame.font.Font(None, 40)
# Render text yang static (tidak berubah)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Definisi rectangle untuk UI elements
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Setup display window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris Game")

# Clock untuk mengontrol frame rate
clock = pygame.time.Clock()

# Inisialisasi game object
game = Game()

# Setup timer event untuk automatic block falling
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop utama
while True:
    # Event handling
    for event in pygame.event.get():
        # Handle window close event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            # Kontrol pergerakan block (hanya jika game tidak over)
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        # Handle automatic block falling
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    # Render score value (dynamic)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    # Fill background
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    # Draw game over text jika game selesai
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    # Draw UI boxes dengan rounded corners (radius 10)
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
        centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    # Draw game elements (grid dan blocks)
    game.draw(screen)

    # Update display
    pygame.display.update()
    # Maintain 60 FPS
    clock.tick(60)