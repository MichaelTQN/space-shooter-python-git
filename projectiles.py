import pygame as pg
class Projectile:

    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y
        self.w = 4
        self.h = 8

    def shoot(self):
        sound_laser.play()

        Projectile = {'x': ship_x + ship_w/2 - projectile.w/2, 
                      'y': ship_y}
        projectiles.append(projectile)

    def move(self):
        self.y -= 8

