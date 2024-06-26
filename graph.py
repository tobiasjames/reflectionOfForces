import math

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np
import pandas as pd
class Graph:
    def __init__(self, rayo, capa):
        self.rayo = rayo
        self.capa = capa
        self.fig = None
        self.ax = None
        self.ani = None
        self.dataframe = None

    def create(self, times):

        # 1) Create a new figure
        self.fig, self.ax = plt.subplots()

        self.ax.spines['left'].set_position(('data', 0))
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)

        # 2) Create figures
        f1_visual = patches.FancyArrowPatch(
            posA=(self.rayo.xy[0], self.rayo.xy[1]),
            posB=(self.rayo.xy[0] + self.rayo.vector[0], self.rayo.xy[1] + self.rayo.vector[1])
        )

        v1 = patches.Arrow(
            x=self.capa.xy[0],
            y=self.capa.xy[1],
            dx=self.capa.top_vector[0] * 100000,
            dy=self.capa.top_vector[1] * 100000,
            color='r'
        )

        v2 = patches.Arrow(
            x=self.capa.xy[0],
            y=self.capa.xy[1],
            dx=self.capa.bottom_vector[0] * 100000,
            dy=self.capa.bottom_vector[1] * 100000,
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


        number_of_frames = times

        positions = self.dataframe["Position"]
        directions = self.dataframe["Direction"]

        def update(frame):

            x = positions[frame][0]
            y = positions[frame][1]
            B_x = x + directions[frame][0]
            B_y = y + directions[frame][1]

            f1_visual.set_positions(
                posA=(x, y),
                posB=(B_x, B_y)
            )

            return f1_visual


        # 6) Create a FuncAnimation, passing the Figure and the animation function.
        self.ani = animation.FuncAnimation(
            fig=self.fig,
            func=update,
            interval=2,
            frames=np.arange(0, number_of_frames + 1, 1)
        )





    def setDataframe(self, dataframe):
        self.dataframe = dataframe
    def show(self):
        # 7) Save or show the animation using one of the following methods:
        # 8) Display the plot
        plt.show()





