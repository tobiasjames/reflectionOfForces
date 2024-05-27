import numpy as np
from graph import Graph
from time import sleep
import pandas as pd

## maybe I need to pass a function as a parameter to either the step or run methods.
# the function I would need to pass would be to update the animation of the graph.

class Sim:
    def __init__(self, capa, fuerza, sleep=1.0):
        self.capa = capa
        self.fuerza = fuerza
        self.count = 0
        self.vector = self.capa.vector1
        self.sleep = sleep
        self.data = pd.DataFrame(
            {
                "Position": [
                    self.fuerza.xy
                ],
                "Direction": [
                    self.fuerza.vector
                ]
            }
        )
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

            # maybe put it into a pandas dataframe?
            #print("Position: " + str(self.fuerza.xy) + " Direction: " + str(self.fuerza.vector))
            temp = pd.DataFrame(
                {
                    "Position": [
                        self.fuerza.xy
                    ],
                    "Direction": [
                        self.fuerza.vector
                    ]
                }
            )

            self.data = pd.concat([self.data, temp], ignore_index=True)

        else:
            self.fuerza.move(
                border_vector=self.vector,
                capa=self.capa
            )
            self.fuerza.reflect(border_vector=self.vector)
            self.vector = self.capa.vector1

            temp = pd.DataFrame(
                {
                    "Position": [
                        self.fuerza.xy
                    ],
                    "Direction": [
                        self.fuerza.vector
                    ]
                }
            )

            self.data = pd.concat([self.data, temp], ignore_index=True)


    def run(self, times):

        for i in range(times):
            self.step()

        self.graph.setDataframe(self.data)
        # print(self.graph.dataframe)
        self.graph.create(times)
        self.graph.show()



