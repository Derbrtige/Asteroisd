import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # --- use pygame groups ---
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # register containers (must be tuples of pygame Groups)
    Player.containers       = (updatable, drawable)
    Asteroid.containers     = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # creates & auto-registers into 'updatable' via Sprite.__init__
    asteroid_field = AsteroidField()

    # creates & auto-registers into updatable/drawable via CircleShape.__init__
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
            for shot in shots:
                if shot.collides_with(asteroid):
                    children = asteroid.split()
                    asteroid.kill()
                    shot.kill()

        # draw everything that knows how to draw itself
        screen.fill((0, 0, 0))
        for obj in drawable:        # can't use Group.draw() because you use custom draw()
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()

if __name__ == "__main__":
    main()
