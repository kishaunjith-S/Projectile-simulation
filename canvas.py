from tkinter import *
import math, time

class CustomCanvas(Canvas):
    g = 9.81

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.start_x = self.start_y = -1
        self.prev_x = self.prev_y = -1
        self.dx = self.dy = -1
        self.prev_line = None
        self.velx = self.vely = self.vel = 0
        self.theta = 0

        self.max_len = 250

        self.ball = None

        self.is_running = False

        self.bind("<ButtonPress-1>", self.set_starting_pos)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<B1-Motion>", self.draw_arrow)

    def on_release(self, e):
        if self.dx is None or self.dy is None: return
        self.delete("old")
        self.delete("ball")

        # region Summon ball

        radius = self.master.rad_var.get()
        st_x = self.start_x
        st_y = self.start_y

        end_x = 2 * radius + self.start_x
        end_y = self.start_y - 2 * radius

        self.ball = self.create_oval(st_x, st_y, end_x, end_y, fill="black", tags="ball")
        # self.is_running = True

        # endregion

        len = math.sqrt(self.dx**2 + self.dy**2)
        self.vel = len / 4

        self.velx = self.vel * math.cos(self.theta)
        self.vely = self.vel * math.sin(self.theta)


        # region move ball

        t = 0
        
        while True:
            t += 1/60
            if t >= 1: break
            
            try: 
                ballx, bally = self.coords("ball")[:2]

                self.vely += self.g / 5

                self.moveto("ball", ballx + self.velx, bally + self.vely)
                self.update()
                time.sleep(1/60)
            except: continue

        self.is_running = False
        self.delete("ball")

        # endregion

        self.dx = self.dy = None

    def set_starting_pos(self, e):
        # if self.is_running: return
        self.prev_x, self.prev_y = self.start_x, self.start_y = e.x, e.y

    def draw_arrow(self, e):
        # if self.is_running: return
        x, y = e.x, e.y
        re_y = y - self.start_y
        re_x = x - self.start_x

        self.theta = math.atan2(re_y, re_x)

        if math.sqrt(re_x ** 2 + re_y ** 2) > self.max_len:

            re_x = self.max_len * math.cos(self.theta)
            x = self.start_x + re_x
            re_y = self.max_len * math.sin(self.theta)
            y = self.start_y + re_y

        self.dx, self.dy = re_x, re_y

        self.delete("old")
        l = self.create_line(self.start_x, self.start_y, x, y, width=7, arrow=LAST, arrowshape=(7, 15, 7), smooth=True, tags="old")
        self.prev_line = l
        self.prev_x, self.prev_y = e.x, e.y
