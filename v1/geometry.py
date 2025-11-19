import settings

import math

def sqdistance3(pointA, pointB=[0, 0, 0]):
    x = pointA[0] - pointB[0]
    y = pointA[1] - pointB[1]
    z = pointA[2] - pointB[2]

    square_distance = x**2 + y**2 + z**2
    return square_distance


def distance3(pointA, pointB=[0, 0, 0]):
    square_distance = sqdistance3(pointA, pointB)
    distance = square_distance**(1/2)
    return distance


def dotproduct3(vectorA, vectorB):
    x = vectorA[0] * vectorB[0]
    y = vectorA[1] * vectorB[1]
    z = vectorA[2] * vectorB[2]

    dot_product = x + y + z
    return dot_product


def crossproduct3(vectorA, vectorB):
    x = vectorA[1] * vectorB[2] - vectorA[2] * vectorB[1]
    y = vectorA[2] * vectorB[0] - vectorA[0] * vectorB[2]
    z = vectorA[0] * vectorB[1] - vectorA[1] * vectorB[0]

    cross_product = [x, y, z]
    return cross_product


def normalize3(vector):
    magnitude = distance3(vector)
    if magnitude != 0:
        x = vector[0] / magnitude
        y = vector[1] / magnitude
        z = vector[2] / magnitude
    else:
        x, y, z = 0, 0, 0
    return [x, y, z]


def project(point):
    t = - settings.focus_point[2] / (point[2] - settings.focus_point[2])
    x = settings.focus_point[0] + t * (point[0] - settings.focus_point[0])
    y = settings.focus_point[1] + t * (point[1] - settings.focus_point[1])
    projected_point = [x, y] 
    return projected_point


def project_sphere(point, radius):
    center2D = project(point)
    radius2D = 320 * radius * math.asin(1 / (point[2] - settings.focus_point[2]))
    rect = [center2D[0] - radius2D, center2D[1] - radius2D, 2 * radius2D, 2 * radius2D]
    return rect