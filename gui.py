import sys
import pygame
import ecu
import config
import time

SIZE = width, height = 120, 160
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


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


def rpmColor(surface, rpm):

    if (rpm < 4000):
        color = BLACK
        surface.fill(BLACK)
    elif (rpm >= 4000 and rpm < 5000):
        color = GREEN
        surface.fill(color)
    elif (rpm >= 5000 and rpm < 6000):
        color = RED
        surface.fill(color)
    elif (rpm >= 6000):
        color = BLUE
        surface.fill(color)


class Tachometer:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface, rpm):
        rpm_text = "{}rpm".format(int(rpm))
        draw_text(surface, rpm_text, self.font,
                  WHITE, (60, 140), "center")


class Spedometer:
    def __init__(self):
        self.speedFont = pygame.font.Font(None, 60)
        self.textFont = pygame.font.Font(None, 30)

    def draw(self, surface, speed):
        speed_text = "{}".format(int(speed))
        draw_text(surface, speed_text, self.speedFont,
                  WHITE, (60, 70), "center")
        draw_text(surface, "Km/h", self.textFont, WHITE, (60, 100), "center")


class WaterTemp:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface, temp):
        level_text = "{0:>3}°C".format(temp)
        color = BLUE
        if temp > 100:
            color = RED
        elif temp > 85:
            color = GREEN
        draw_text(surface, level_text, self.font, color, (90, 20), "center")


class Battery:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface, battery):
        battery_text = "{}V".format(float(battery))
        draw_text(surface, battery_text, self.font,
                  WHITE, (30, 20), "center")


if __name__ == '__main__':

    ecuObject = ecu.ecuThread()

    while not config.ecuReady:
        time.sleep(.01)

    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)

    speedo = Spedometer()
    tach = Tachometer()
    waterTemp = WaterTemp()
    battery = Battery()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ecuObject.closeConnection()
                pygame.quit()
                sys.exit()


        SCREEN.fill(BLACK)
        rpmColor(SCREEN, ecuObject.rpm)
        draw_grid(SCREEN)

        speedo.draw(SCREEN, ecuObject.speed)
        tach.draw(SCREEN, ecuObject.rpm)
        waterTemp.draw(SCREEN, ecuObject.coolant_temp)
        battery.draw(SCREEN, 12.2)

        pygame.display.update()
