import numpy as np
from graph import Graph
from time import sleep

## maybe I need to pass a function as a parameter to either the step or run methods.
# the function I would need to pass would be to update the animation of the graph.

class Sim:
    def __init__(self, capa, fuerza, sleep=1.0):
        self.capa = capa
        self.fuerza = fuerza
        self.count = 0
        self.vector = self.capa.vector1
        self.sleep = sleep
        self.graph = Graph(fuerza=self.fuerza, capa=self.capa)

    def step(self):

        which_vector = np.all(self.vector == self.capa.vector1)
        if (
            which_vector
        ):

            self.fuerza.move(
                border_vector=self.vector,
                capa=self.capa
            )
            self.fuerza.reflect(border_vector=self.vector)

            self.count = self.count + 1
            self.vector = self.capa.vector2

            print("Position: " + str(self.fuerza.xy) + " Direction: " + str(self.fuerza.vector))

        else:
            self.fuerza.move(
                border_vector=self.vector,
                capa=self.capa
            )
            self.fuerza.reflect(border_vector=self.vector)
            self.vector = self.capa.vector1
            print("Position: " + str(self.fuerza.xy) + " Direction: " + str(self.fuerza.vector))

        self.graph.show()

        # I need to "update the graph" to show the "new" fuerza
        # - it should already be "updated" because of the parameter I passed to Graph() when constructing the Sim()
        # self.graph.update(fuerza=self.fuerza)



    def run(self):

        for i in range(5):
            self.step()



