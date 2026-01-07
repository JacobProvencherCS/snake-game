import pyglet
from random import choice
from itertools import product

RED = (255, 0, 0)

class Cube:

    def __init__(self, position, direction=(1, 0), color=RED) -> None:
        pass

    def move(self, direction):
        pass

    def draw(self, surface, eyes=False):
        pass

class Snake:

    def __init__(self) -> None:
        pass

    def move(self, direction):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass

class Apple:

    def __init__(self) -> None:
        pass

    def spawn(self, snake):
        pass

class Window:

    def __init__(self) -> None:
        pass
    
    def draw_grid(self):
        pass

    def redraw_window(self):
        pass

    def mainloop(self):
        pass


if __name__ == '__main__':
    
    game = Window((500, 500), 20)
    game.mainloop()

    pyglet.quit()







