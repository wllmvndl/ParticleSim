import geometry
import settings

import pygame

def gravity(particleA, particleB):
    square_distance = geometry.sqdistance3(particleA.position, particleB.position)
    
    force = settings.gravitation * particleB.mass / (square_distance + 1)
    
    return force


def electromagnetic(particleA, particleB):
    if particleA.electromagnetic == False or particleB.electromagnetic == False:
        return 0
    
    force = - settings.couloumb * particleA.em_charge * particleB.em_charge

    distance = geometry.distance3(particleA.position, particleB.position)
    distance /= 100
    
    force /= (distance**2 + 1)
    return force


def strong(particleA, particleB):
    if particleA.strong == False or particleB.strong == False:
        return 0

    distance = geometry.distance3(particleA.position, particleB.position)
    distance -= 10
    distance /= 10
    force = settings.strong * distance / (distance**2 + 1)

    if particleA.color_charge == particleB.color_charge:
        force *= -2

    return force