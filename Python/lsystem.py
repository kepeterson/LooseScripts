from Tkinter import *
import time
import math
__author__ = 'kpeterson'

CHARACTERS = '10'
CONSTANTS = '[]'
SEED = '0'
STACK = []
PI = math.pi
LINE_LENGTH = 20
ITERATIONS = 5
ANGLE_OFFSET = PI/4


class App(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.configure(background='black')
        self.canvas.pack()
        self.angle = PI/2
        self.root.bind("<Key>", self.quit)
        self.root.after(0, self.animation)
        self.root.mainloop()

    @staticmethod
    def step_it(char):
        if char in CONSTANTS:
            return char
        if char == '1':
            return '11'
        if char == '0':
            return '1[0]0'

    def animation(self):
        start = (300, 600)
        advance = True
        i = 0
        global SEED
        while advance:
            for char in SEED:
                end = self.draw(char, start)
                start = end
            self.canvas.update()
            time.sleep(.5)
            if i >= ITERATIONS:
                advance = False
            seed_list = [self.step_it(ch) for ch in SEED]
            SEED = ''.join(seed_list)
            start = (300, 600)
            self.angle = PI/2
            i += 1

    def draw(self, char, position):
        if char == '0':
            return self.draw_line(position, self.angle)
        if char == '1':
            return self.draw_line(position, self.angle)
        if char == '[':
            STACK.append((position, self.angle))
            self.angle += ANGLE_OFFSET
            return position
        if char == ']':
            position, pre_angle = STACK.pop()
            self.angle = pre_angle - ANGLE_OFFSET
            return position

    def draw_line(self, start, angle):
        x, y = start
        end = (x - LINE_LENGTH * math.cos(angle), y - LINE_LENGTH * math.sin(angle))
        self.canvas.create_line(start, end,
                                fill='red', width=10)
        return end

    def quit(self, event):
        if event.char == ' ':
            self.root.destroy()

if __name__ == "__main__":
    App()