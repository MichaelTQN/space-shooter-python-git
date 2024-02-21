import pygame as pg
class Alien:
    def __init__(self, x, y, hitpoints=2):
        self.x = x
        self.y = y 
        self.hp = hitpoints
        self.draw_tick = 0
        self.images = []

        # Alien character
        for i in range(2):
            img = pg.image.load(f"images/alien_{i}.png")
            self.images.append(img)

        self.w = self.images[0].get_rect().size[0]
        self.h = self.images[0].get_rect().size[1]

    def move(self):
        self.x += 0
        self.y += 1 
        


    def draw(self, screen):
        r = int(self.draw_tick/8) % 2
        screen.blit(self.images[r], (self.x, self.y))
        self.draw_tick += 1