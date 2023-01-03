from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import ST7735
import sys
import config


SIZE = width, height = 128, 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)





def draw_text(surface, text, fontObj, color, pos, position="center"):

    surface.text(pos, text, fill=color, font=fontObj,
                 align=position, anchor='mm')


def draw_grid(surface):
    # horizontal lines
    surface.line([(0, 40), (120, 40)], fill=WHITE, width=1)
    surface.line([(0, 120), (120, 120)], fill=WHITE, width=1)

    # vertical lines
    surface.line([(60, 0), (60, 40)], fill=WHITE, width=1)


def rpmColor(surface, rpm):

    if (rpm < 4000):
        color = BLACK
        surface.rectangle([(0, 0), (128, 160)], fill=color,
                          outline=None, width=0)
    elif (rpm >= 4000 and rpm < 5000):
        color = GREEN
        surface.rectangle([(0, 0), (128, 160)], fill=color,
                          outline=None, width=0)
    elif (rpm >= 5000 and rpm < 6000):
        color = RED
        surface.rectangle([(0, 0), (128, 160)], fill=color,
                          outline=None, width=0)
    elif (rpm >= 6000):
        color = BLUE
        surface.rectangle([(0, 0), (128, 160)], fill=color,
                          outline=None, width=0)


class Tachometer:
    def __init__(self):
        self.font = ImageFont.truetype(
            '/usr/share/fonts/truetype/roboto/slab/RobotoSlab-Regular.ttf', 25)

    def draw(self, surface, rpm):
        rpm_text = "{}rpm".format(int(rpm))
        draw_text(surface, rpm_text, self.font,
                  WHITE, (60, 140), "center")


class Spedometer:
    def __init__(self):
        self.speedFont = ImageFont.truetype(
            '/usr/share/fonts/truetype/roboto/slab/RobotoSlab-Regular.ttf', 50)
        self.textFont = ImageFont.truetype(
            '/usr/share/fonts/truetype/roboto/slab/RobotoSlab-Regular.ttf', 20)

    def draw(self, surface, speed):
        speed_text = "{}".format(int(speed))
        draw_text(surface, speed_text, self.speedFont,
                  WHITE, (60, 70), "center")
        draw_text(surface, "Km/h", self.textFont, WHITE, (60, 100), "center")


class WaterTemp:
    def __init__(self):
        self.font = ImageFont.truetype(
            '/usr/share/fonts/truetype/roboto/slab/RobotoSlab-Regular.ttf', 25)

    def draw(self, surface, temp):
        level_text = "{0:>3}".format(temp)
        color = BLUE
        if temp > 100:
            color = RED
        elif temp > 85:
            color = GREEN
        draw_text(surface, level_text, self.font, color, (90, 20), "center")


class FuelLevel:
    def __init__(self):
        self.font = ImageFont.truetype(
            '/usr/share/fonts/truetype/roboto/slab/RobotoSlab-Regular.ttf', 25)

    def draw(self, surface, fuel_level):
        fuel_text = "{}%".format(int(fuel_level))
        draw_text(surface, fuel_text, self.font,
                  WHITE, (30, 20), "center")


if __name__ == "__main__":

    
    
    # Create ST7735 LCD display class.
    disp = ST7735.ST7735(
        port=0,
        cs=0,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
        dc=25,
        # 18 for back BG slot, 19 for front BG slot.
        backlight=18,
        rotation=0,
        rst=27,
        width=128, height=160,
        spi_speed_hz=10000000,
        invert=False
    )
    
    disp.begin()

    img = Image.new('RGBA', SIZE, color=BLACK)

    speedo = Spedometer()
    tach = Tachometer()
    waterTemp = WaterTemp()
    fuel = FuelLevel()

    SCREEN = ImageDraw.Draw(img)

    while not config.exit_loop:

        rpmColor(SCREEN, 4)
        draw_grid(SCREEN)

        speedo.draw(SCREEN, 5)
        tach.draw(SCREEN, 6)
        waterTemp.draw(SCREEN, 5)
        fuel.draw(SCREEN, 8)

        disp.display(img)
    
    
    print("uscendo")
    sys.exit()
