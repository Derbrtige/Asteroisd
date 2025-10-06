import pygame
from constants import *
from player import Player

class Group(list):
    def update(self, dt):
        # iterate over a copy so objects can remove themselves safely
        for obj in self[:]:
            if hasattr(obj, "update"):
                obj.update(dt)

    def draw(self, screen):
        for obj in self:
            if hasattr(obj, "draw"):
                obj.draw(screen)

def main():
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = Group()
    drawable  = Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0, 0, 0))
        drawable.draw(screen)
        pygame.display.flip()
        dt =  clock.tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
