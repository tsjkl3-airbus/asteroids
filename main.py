import pygame
from player import Player
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)
        pygame.time.Clock().tick(60)
        dt = pygame.time.Clock().tick(60) / 1000.0
        pygame.display.flip()

if __name__ == "__main__":
    main()
