import pygame
from random import randint

pygame.init()
pygame.font.init()

WIDTH = 604
HEIGHT = WIDTH + 30
CENTER = (WIDTH // 2, WIDTH // 2)
RADIUS = WIDTH // 2 - 1
TITLE = "Pi Calculator Using Darts"
ICON = pygame.image.load('Pi-Calculation/darts.png')  # !!Path of icon
FONT = pygame.font.SysFont('Arial', 20)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def setWindow(TITLE):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)


def distance(point, center=CENTER):
    return ((point[0] - center[0])**2 + (point[1] - center[1])**2)**0.5


def main():
    setWindow(TITLE)

    RUNNING = True
    NO_OF_POINTS = 100
    total_points = 0
    inside_circle = 0

    while RUNNING:
        for event in pygame.event.get():
            RUNNING = False if event.type == pygame.QUIT else True

        pygame.draw.circle(SCREEN, BLACK, CENTER, RADIUS, 1)

        total_points += NO_OF_POINTS
        for i in range(NO_OF_POINTS):
            point = (randint(2, WIDTH - 1), randint(2, HEIGHT - 30 - 1))
            color = RED if distance(point) >= RADIUS else GREEN
            inside_circle += 1 if distance(point) <= RADIUS else 0
            pygame.draw.circle(SCREEN, color, point, 1)

        pygame.draw.rect(SCREEN, WHITE, (0, HEIGHT - 30, WIDTH, 30))
        pi_estimate = float(4 * inside_circle / total_points)
        pi_label = FONT.render(
            "PI: " + "{:.20f}".format(pi_estimate), True, BLACK, WHITE)
        SCREEN.blit(pi_label, (0, WIDTH))
        pygame.display.update()

if __name__ == '__main__':
    main()
