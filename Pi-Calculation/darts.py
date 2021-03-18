import pygame
from random import randint

pygame.init()
pygame.font.init()


HEIGHT = WIDTH = 604
CENTER = (HEIGHT//2, WIDTH//2)
RADIUS = HEIGHT//2-1
TITLE = "Pi Calculator Using Darts"

# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def setTitle(TITLE):
    pygame.display.set_caption(TITLE)


def setIcon(ICON):
    pygame.display.set_icon(ICON)


def distance(point, center=CENTER):
    return float((point[0]-center[0])**2) + float((point[1]-center[1])**2)


def main():
    setTitle(TITLE)
    # setIcon(ICON)

    running = True
    no_of_points = 0
    inside_circle = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(SCREEN, BLACK, CENTER, RADIUS, 1)

        for i in range(10000):
            point = (randint(2, WIDTH-1), randint(2, HEIGHT-1))
            if distance(point)**0.5 >= RADIUS:
                pygame.draw.circle(SCREEN, RED, point, 0)
            else:
                inside_circle += 1
                pygame.draw.circle(SCREEN, GREEN, point, 0)
        no_of_points += 10000

        print(float(4*inside_circle/no_of_points))
        pygame.display.update()


main()
