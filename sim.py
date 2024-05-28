import numpy as np
from graph import Graph
from time import sleep
import pandas as pd

## maybe I need to pass a function as a parameter to either the step or run methods.
# the function I would need to pass would be to update the animation of the graph.

class Sim:
    def __init__(self, capa, rayo, sleep=1.0):
        self.capa = capa
        self.rayo = rayo
        self.count = 0
        self.vector = self.capa.top_vector
        self.sleep = sleep
        self.data = pd.DataFrame(
            {
                "Position": [
                    self.rayo.xy
                ],
                "Direction": [
                    self.rayo.vector
                ]
            }
        )
        self.graph = Graph(rayo=self.rayo, capa=self.capa)

    def step(self):

        # print(self.vector)
        which_vector = np.all(self.vector == self.capa.top_vector)
        if (
            which_vector
        ):

            self.rayo.move(
                border_vector=self.vector,
                capa=self.capa
            )
            self.rayo.reflect(border_vector=self.vector)

            self.count = self.count + 1
            self.vector = self.capa.bottom_vector

            # maybe put it into a pandas dataframe?
            #print("Position: " + str(self.fuerza.xy) + " Direction: " + str(self.fuerza.vector))
            temp = pd.DataFrame(
                {
                    "Position": [
                        self.rayo.xy
                    ],
                    "Direction": [
                        self.rayo.vector
                    ]
                }
            )

            self.data = pd.concat([self.data, temp], ignore_index=True)

        else:
            self.rayo.move(
                border_vector=self.vector,
                capa=self.capa
            )
            self.rayo.reflect(border_vector=self.vector)
            self.vector = self.capa.top_vector

            temp = pd.DataFrame(
                {
                    "Position": [
                        self.rayo.xy
                    ],
                    "Direction": [
                        self.rayo.vector
                    ]
                }
            )


            self.data = pd.concat([self.data, temp], ignore_index=True)



    def run(self, times):

        for i in range(times):
            self.step()

        self.graph.setDataframe(self.data)
        print(self.graph.dataframe)
        self.graph.create(times)
        self.graph.ani.pause()
        self.graph.show()



