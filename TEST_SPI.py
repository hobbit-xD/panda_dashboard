import pygame
import sys
import os


SIZE = width, height = 120, 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_grid(surface):
    # horizontal lines
    pygame.draw.line(surface, WHITE, (0, 40), (120, 40))
    pygame.draw.line(surface, WHITE, (0, 120), (120, 120))

    # vertical lines
    pygame.draw.line(surface, WHITE, (60, 0), (60, 40))

if __name__ == '__main__':

    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(0)
    SCREEN = pygame.display.set_mode(SIZE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        
        SCREEN.fill(BLACK)
        draw_grid(SCREEN)
        
        pygame.display.update()
        



