from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

import ST7735
#import os

import pygame
import sys



SIZE = width, height = 128, 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_text(surface, text, fontObj, color, pos, position="center"):
    textSurfaceObj = fontObj.render(text, True, color, BLACK)
    textSurfaceObj.set_colorkey(BLACK)
    textRectObj = textSurfaceObj.get_rect()
    if position == "center":
        textRectObj.center = pos
    elif position == "topright":
        textRectObj.topright = pos
    elif position == "bottomright":
        textRectObj.bottomright = pos
    elif position == "topleft":
        textRectObj.topleft = pos

    surface.blit(textSurfaceObj, textRectObj)
    

def draw_grid(surface):
    # horizontal lines
    pygame.draw.line(surface, WHITE, (0, 40), (120, 40))
    pygame.draw.line(surface, WHITE, (0, 120), (120, 120))

    # vertical lines
    pygame.draw.line(surface, WHITE, (60, 0), (60, 40))
    



class Spedometer:
    def __init__(self):
        self.speedFont = pygame.font.Font(None, 60)
        self.textFont = pygame.font.Font(None, 30)

    def draw(self, surface, speed):
        speed_text = "{}".format(int(speed))
        draw_text(surface, speed_text, self.speedFont,
                  WHITE, (60, 70), "center")
        draw_text(surface, "Km/h", self.textFont, WHITE, (60, 100), "center")

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=0,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=25,
    backlight=18,               # 18 for back BG slot, 19 for front BG slot.
    rotation=0,
    rst=27,
    width=128, height=160,
    spi_speed_hz=10000000,
    invert=False
)

disp.begin()

#img = Image.new('RGB', (128,160), color=BLACK)

#surface = ImageDraw.Draw(img)

#draw_grid(surface)

pygame.init()
pygame.mouse.set_visible(0)
SCREEN = pygame.display.set_mode(SIZE)
speedo = Spedometer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        
    SCREEN.fill(BLACK)
    draw_grid(SCREEN)
    
    speedo.draw(SCREEN, 35)
    
    strFormat = 'RGBA'
    raw_str = pygame.image.tostring(SCREEN,strFormat,False)
    img = Image.frombytes(strFormat,SCREEN.get_size(),raw_str)
        


    disp.display(img)