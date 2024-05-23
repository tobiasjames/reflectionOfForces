import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np
class Graph:
    def __init__(self, fuerza, capa):
        self.fuerza = fuerza
        self.capa = capa
        self.fig = None
        self.ax = None
        self.ani = None
        self.__create()
    def __create(self):

        # 1) Create a new figure
        self.fig, self.ax = plt.subplots()

        self.ax.spines['left'].set_position(('data', 0))
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)

        # 2) Create figures
        f1_visual = patches.Arrow(
            x=self.fuerza.xy[0],
            y=self.fuerza.xy[1],
            dx=self.fuerza.vector[0],
            dy=self.fuerza.vector[1]
        )

        v1 = patches.Arrow(
            x=self.capa.xy[0],
            y=self.capa.xy[1],
            dx=self.capa.vector1[0] * 100000,
            dy=self.capa.vector1[1] * 100000,
            color='r'
        )

        v2 = patches.Arrow(
            x=self.capa.xy[0],
            y=self.capa.xy[1],
            dx=self.capa.vector2[0] * 100000,
            dy=self.capa.vector2[1] * 100000,
            color='r'
        )

        # 3) Add the figures to the axes
        self.ax.add_patch(f1_visual)
        self.ax.add_patch(v1)
        self.ax.add_patch(v2)

        # 4) Set the limits of the axes
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        # 5) Create an animation function that updates the artists for a given frame. Typically, this calls set_* methods of the artists.
        def update(frame):
            x = self.fuerza.xy[0] + (self.fuerza.distance / self.fuerza.magnitude) * (frame / self.fuerza.vector[0])
            y = self.fuerza.xy[1] + (self.fuerza.distance / self.fuerza.magnitude) * (frame / self.fuerza.vector[1])
            self.fuerza.xy = [x, y]
            return self.fuerza

        # 6) Create a FuncAnimation, passing the Figure and the animation function.
        self.ani = animation.FuncAnimation(
            fig=self.fig,
            func=update,
            interval=20,
            frames=np.arange(0, 10, 1)
        )





    def show(self):
        # 7) Save or show the animation using one of the following methods:
        # 8) Display the plot
        plt.show()





