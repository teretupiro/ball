from tkinter import Tk, Canvas


class Ball:
    SIZE = 20
    COLOR = 'RED'
    X = 200
    Y = 200
    HEIGHT = 250
    WEIGHT = 250
    x_dir = 1
    y_dir = 1

    def __init__(self, canvas, x=200, y=200, color='red', size=20):
        self.canvas = canvas
        self.ball = self.canvas.create_oval(x - size / 2,
                                            y - size / 2,
                                            x + size / 2,
                                            y + size / 2,
                                            fill=color)

    def motion(self, root, delay, WIDTH, HEIGHT):
        self.canvas.move(self.ball, 0, 0)

        self.canvas.move(self.ball, self.x_dir, self.y_dir)
        pos = self.canvas.coords(self.ball)

        if pos[2] >= WIDTH:
            self.x_dir = - self.x_dir

        if pos[0] <= 0:
            self.x_dir = - self.x_dir

        if pos[3] >= HEIGHT:
            self.y_dir = - self.y_dir

        if pos[1] <= 0:
            self.y_dir = - self.y_dir

        root.after(10, lambda: self.motion(root, delay, WIDTH, HEIGHT))


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas()
    canvas.pack()
    ball_red = Ball(canvas)
    ball_blue = Ball(canvas, 100, 100, 'blue')
    ball_green = Ball(canvas, y=50, color='green')
    ball_yellow = Ball(canvas, x=50, color='yellow')
    root.mainloop()
