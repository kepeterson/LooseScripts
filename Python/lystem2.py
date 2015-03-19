from Tkinter import *
import colorsys
import time
import math, random
__author__ = 'kpeterson'


class App(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.configure(background='black')
        self.canvas.pack()
        self.angle = list(START_ANGLES)
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
        starts = [(300, 600), (0, 300), (300, 0), (600, 300),
                  (0, 0), (0, 600), (600, 0), (600, 600)]
        advance = True
        count = 0
        global SEED
        while advance:
            for i, start in enumerate(starts):
                for char in SEED:
                    end = self.draw(char, start, i)
                    start = end
            self.canvas.configure(background=BG.next())
            self.canvas.update()
            time.sleep(FRAMERATE)
            if count >= ITERATIONS:
                time.sleep(5. * FRAMERATE)
                SEED = '0'
                count = 0
                self.canvas.delete("all")
                global COLORS, ANGLE_OFFSET
                COLORS = COLORSRING.next()
                ANGLE_OFFSET = OFFSETS.random()
            seed_list = [self.step_it(ch) for ch in SEED]
            SEED = ''.join(seed_list)
            self.angle = list(START_ANGLES)
            count += 1

    def draw(self, char, position, i):
        if char == '0':
            return self.draw_line(position, self.angle[i])
        if char == '1':
            return self.draw_line(position, self.angle[i])
        if char == '[':
            STACK.append((position, self.angle[i]))
            self.angle[i] += ANGLE_OFFSET
            return position
        if char == ']':
            position, pre_angle = STACK.pop()
            self.angle[i] = pre_angle - ANGLE_OFFSET
            return position

    def draw_line(self, start, angle):
        x, y = start
        end = (x - LINE_LENGTH * math.cos(angle), y - LINE_LENGTH * math.sin(angle))
        self.canvas.create_line(start, end,
                                fill=COLORS.random(), width=10)
        return end

    def quit(self, event):
        if event.char == ' ':
            self.root.destroy()


class Ring:
    def __init__(self, ring):
        self.ring = ring
        self.i = 0

    def next(self):
        if self.i == len(self.ring) - 1:
            self.i = 0
            return self.ring[0]
        else:
            self.i += 1
            return self.ring[self.i]

    def random(self):
        return random.choice(self.ring)


class Slow:
    def __init__(self, ring):
        self.ring = ring
        self.i = 0
        self.start = ring.next()
        self.end = ring.next()

    def next(self):
        m1 = self.start.split('#')[1]
        m2 = self.end.split('#')[1]
        rbg1 = get_rbg(m1)
        rbg2 = get_rbg(m2)
        hex_color = hexify(rbg1, rbg2, self.i)
        self.i += 1
        if self.i == BG_EVOLVE:
            self.i = 0
            self.start = self.end
            self.end = self.ring.next()
        return '#'+hex_color


def get_rbg(hex_str):
    return int(hex_str[:2], 16), int(hex_str[2:4], 16), int(hex_str[4:], 16)


def hexify(rbg1, rbg2, i):
    hsv1 = colorsys.rgb_to_hsv(*normalize_rbg(rbg1))
    hsv2 = colorsys.rgb_to_hsv(*normalize_rbg(rbg2))
    final_hsv = (hsv1[0] + float(i)/BG_EVOLVE * (hsv2[0] - hsv1[0]),
                 hsv1[1] + float(i)/BG_EVOLVE * (hsv2[1] - hsv1[1]),
                 hsv1[2] + float(i)/BG_EVOLVE * (hsv2[2] - hsv1[2]))
    final_rbg = unnormalize_rbg(colorsys.hsv_to_rgb(*final_hsv))
    color_str = ''.join([hex_convert(x) for x in final_rbg])
    return color_str


def normalize_rbg(rgb):
    return rgb[0]/255., rgb[1]/255., rgb[2]/255.


def unnormalize_rbg(rgb):
    return int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)


def hexify2(rgb):
    r, g, b = rgb


def hex_convert(a):
    ret = hex(a).split('x')[1]
    if a <= 15:
        ret = '0' + ret
    return ret

CHARACTERS = '10'
FRAMERATE = 1./60.
CONSTANTS = '[]'
SEED = '0'
BG_EVOLVE = 4.
STACK = []
PI = math.pi
LINE_LENGTH = 20
ITERATIONS = 7
START_ANGLES = (PI/2, PI, 3*PI/2, 2*PI, 5./4. * PI, 3./4. * PI,
                7./4. * PI, 1./4. * PI)
ANGLE_OFFSET = 1./4. * PI
OFFSETS = Ring([PI * (float(n)+1.)/12. for n in range(10)])
COLORS1 = Ring(['#C14347', '#CD545B', '#C973A4', '#A159A4', '#D99D81'])
COLORS2 = Ring(['#5C56CE', '#7D56CC', '#9594CE', '#9AC0AA'])
COLORS3 = Ring(['#5ECFA2', '#4AC3C0', '#40B154', '#98BC94'])
COLORS4 = Ring(['#5FCC47', '#A5C744', '#348028', '#9FDE7D'])
COLORSRING = Ring([COLORS1, COLORS2, COLORS3, COLORS4])
COLORS = COLORSRING.next()
BG = Slow(Ring(['#D0D0E3', '#C1D0DF', '#EBEAF5']))

if __name__ == "__main__":
    App()