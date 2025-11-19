import forces
import geometry
import settings

import pygame
import random

class Particle:
    def __init__(self, simulation, position, velocity=[0, 0, 0]):
        self.simulation = simulation

        self.electromagnetic = False
        self.strong = False

        self.mass = 1
        self.radius = 10
        self.color = (100, 80, 100)

        print(position)

        self.position = [position[0], position[1], position[2]]
        self.velocity = [velocity[0], velocity[1], velocity[2]]

    def move(self):
        for n in range(3):
            self.position[n] += self.velocity[n] * settings.delta_time

            if self.position[n] < 10:
                self.position[n] = 10
                self.velocity[n] *= -1

            elif self.position[n] > settings.world_dimensions[n] - 10:
                self.position[n] = settings.world_dimensions[n] - 10
                self.velocity[n] *= -1

            self.velocity[n] *= settings.damping

    def interact(self):
        for other in self.simulation.particles:
            if other != self and self.mass != 0:
                sum_forces = 0
                sum_forces += forces.gravity(self, other)
                sum_forces += forces.strong(self, other)
                sum_forces += forces.electromagnetic(self, other)

                relative_position = [other.position[0] - self.position[0], other.position[1] - self.position[1], other.position[2] - self.position[2]]
                relative_normal = geometry.normalize3(relative_position)

                self.velocity[0] += sum_forces * geometry.dotproduct3(relative_normal, [1, 0, 0]) / self.mass
                self.velocity[1] += sum_forces * geometry.dotproduct3(relative_normal, [0, 1, 0]) / self.mass
                self.velocity[2] += sum_forces * geometry.dotproduct3(relative_normal, [0, 0, 1]) / self.mass

    def draw(self):
        if self.position[2] < 0:
            return

        rect = geometry.project_sphere(self.position, self.radius)
        pygame.draw.ellipse(self.simulation.screen, self.color, rect)


class Electron(Particle):
    def __init__(self, simulation, position=[0, 0, 0], velocity=[0, 0, 0]):
        super().__init__(simulation, position, velocity)

        self.electromagnetic = True
        
        self.mass = 1
        self.radius = 10
        self.em_charge = -1
        self.color = (120, 100, 200)


class Quark(Particle):
    def __init__(self, simulation, color_charge, position, velocity=[0, 0, 0]):
        super().__init__(simulation, position, velocity)

        self.electromagnetic = True
        self.strong = True
        
        self.color_charge = color_charge

        if color_charge == "red":
            self.color = (255, 50, 50)
        if color_charge == "green":
            self.color = (50, 255, 50)
        if color_charge == "blue":
            self.color = (50, 50, 255)


class UpQuark(Quark):
    def __init__(self, simulation, color_charge, position, velocity=[0, 0, 0]):
        super().__init__(simulation, color_charge, position, velocity)

        self.mass = 20
        self.radius = 15
        self.em_charge = 2/3

class DownQuark(Quark):
    def __init__(self, simulation, color_charge, position, velocity=[0, 0, 0]):
        super().__init__(simulation, color_charge, position, velocity)

        self.mass = 22
        self.radius = 16
        self.em_charge = -1/3


class Nucleon:
    def __init__(self, simulation, is_proton, position, velocity=[0, 0, 0]):
        
        colors = ["red", "blue", "green"]
        random.shuffle(colors)

        position1 = [position[0] + random.uniform(-1, 1), position[1] + random.uniform(-1, 1), position[2] + random.uniform(-1, 1)]
        position2 = [position[0] + random.uniform(-1, 1), position[1] + random.uniform(-1, 1), position[2] + random.uniform(-1, 1)]
        position3 = [position[0] + random.uniform(-1, 1), position[1] + random.uniform(-1, 1), position[2] + random.uniform(-1, 1)]

        simulation.particles.append(UpQuark(simulation, colors[0], position1, velocity))        
        simulation.particles.append(DownQuark(simulation, colors[1], position2, velocity))

        if is_proton:
            simulation.particles.append(UpQuark(simulation, colors[2], position3, velocity))
        else:
            simulation.particles.append(DownQuark(simulation, colors[2], position3, velocity))