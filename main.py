#!/usr/bin/python3
# -*- coding: utf-8 -*

"""Geometry-Dash game with pygame."""

import os
import tkinter as tk

from pygame import *

init()

# Setup display

root = tk.Tk()

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

HEIGHT = 600
WIDTH = 1200

win_x = screen_width // 2 - WIDTH // 2
win_y = screen_height // 2 - HEIGHT // 2

os.environ["SDL_VIDEO_WINDOW_POS"] = str(win_x) + ',' + str(win_y)
win = display.set_mode((WIDTH, HEIGHT)) # main window
display.set_caption("Geometry-Dash")

bg = image.load("Images/background.jpg")
bg_rect = bg.get_rect(center = (WIDTH//2, HEIGHT//2))

ground = Surface((WIDTH * 2, HEIGHT * 3//10))
ground_rect = ground.get_rect(bottomleft = (0, HEIGHT))
ground_img = transform.scale(image.load("Images/ground.jpg"), (ground_rect.w // 2, ground_rect.h))
ground_img_rect = ground_img.get_rect(topleft = (0, 0))
ground.blit(ground_img, ground_img_rect)
ground_img_rect = ground_img.get_rect(topleft = (ground_rect.centerx, 0))
ground.blit(ground_img, ground_img_rect)

def move_ground(rect):
    """Move the ground each frame"""

    rect.x -= 10

    if rect.centerx == 0:
        rect.left = 0

class Icon:
    """The square to move"""

    def __init__(self, img_location, bottom):
        self.size = 100
        self.image = transform.scale(image.load(img_location), (self.size, self.size))
        self.x = self.size * -1
        self.y = bottom - self.size
        self.position = (self.x, self.y)

    def move(self):
        self.x += 10
        self.position = (self.x, self.y)

icon = Icon("Images/icon.png", HEIGHT - ground_img_rect.h)

# Setup game loop

FPS = 60
clock = time.Clock()
run = True

while run:
    clock.tick(FPS)

    for e in event.get():
            if e.type == QUIT: 
                run = False

    if icon.x < WIDTH * 2//10:
        icon.move()

    move_ground(ground_rect)

    win.blit(bg, bg_rect)
    win.blit(ground, ground_rect)
    win.blit(icon.image, icon.position)
    display.update()

quit()