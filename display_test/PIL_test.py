from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

import ST7735
#import os


SIZE = width, height = 128, 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_grid(surface):
    # horizontal lines
    surface.line([(0, 40), (120, 40)], fill=WHITE, width=1)
    surface.line([(0, 120), (120, 120)], fill=WHITE, width=1)

    # vertical lines
    surface.line([(60, 0), (60, 40)], fill=WHITE, width=1)


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

img = Image.new('RGB', (128,160), color=BLACK)

surface = ImageDraw.Draw(img)

draw_grid(surface)

disp.display(img)