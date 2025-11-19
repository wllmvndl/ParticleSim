import objects
import settings

import pygame
import random
import sys

class Simulation:  
    def __init__(self):
        pygame.init()
        self.FPS = settings.FPS

        self.screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])
        pygame.display.set_caption("3D Particle Sim")

        self.particles = [objects.Electron(self, [settings.screen_width / 2, settings.screen_height / 2, settings.screen_depth / 2], [0, 0, -10])]

    # Game functions
    def process_input(self):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                return False
                        
            elif event.type == pygame.KEYDOWN:  
                self.key_pressed = pygame.key.get_pressed()

                if event.key == pygame.K_ESCAPE:
                    return False

                if event.key == pygame.K_r:
                    self.particles = []

                if event.key == pygame.K_SPACE:
                    random_position = [random.random() * settings.screen_width, random.random() * settings.screen_height, random.random() * settings.screen_depth]
                    random_velocity = [random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10]
                    self.particles.append(objects.Electron(self, random_position, random_velocity))

                if event.key == pygame.K_p:
                    random_position = [random.random() * settings.screen_width, random.random() * settings.screen_height, random.random() * settings.screen_depth]
                    random_velocity = [random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10]
                    objects.Nucleon(self, True, random_position, random_velocity)

                if event.key == pygame.K_n:
                    random_position = [random.random() * settings.screen_width, random.random() * settings.screen_height, random.random() * settings.screen_depth]
                    random_velocity = [random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10, random.uniform(-1, 1) * 10]
                    objects.Nucleon(self, False, random_position, random_velocity)
                
        return True

    def update(self):
        for particle in self.particles:
            particle.move()

        for particle in self.particles:
            particle.interact()

    def draw(self):
        self.screen.fill((5, 0, 10))

        self.particles.sort(key=lambda particle: particle.position[2], reverse=True)

        for particle in self.particles:
            particle.draw()

    def game_loop(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            running = self.process_input()
            self.update()
            self.draw()

            pygame.display.flip()
            clock.tick(self.FPS)

        pygame.quit()
        sys.exit()


# Create and Run Simulation
sim = Simulation()

if __name__ == "__main__":
    sim.game_loop()