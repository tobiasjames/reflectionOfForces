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
        self.border_vector = self.capa.top_vector
        self.sleep = sleep
        self.data = pd.DataFrame(
            {
                "Position": [
                    self.rayo.xy
                ],
                "Direction": [
                    self.rayo.vector
                ],
                "Times": [
                    0
                ]
            }
        )
        self.graph = Graph(rayo=self.rayo, capa=self.capa)
        self.count = 0

    def step(self, delta_t=0.01):

        self.count = self.count + 1

        self.rayo.move(border_vector=self.border_vector)
        self.rayo.reflect(border_vector=self.border_vector)

        clock = 0

        while (clock < self.rayo.time):

            self.count = self.count + 1
            clock = clock + delta_t

            last = self.data.shape[0] - 1
            temp = pd.DataFrame(
                {
                    "Position": [
                        self.data["Position"][last] + delta_t * self.data["Direction"][last]
                    ],
                    "Direction": [
                        self.data["Direction"][last]
                    ],
                    "Times": [
                        self.data["Times"][last] + delta_t
                    ]
                }
            )

            self.data = pd.concat([self.data, temp], ignore_index=True)


        temp = pd.DataFrame(
            {
                "Position": [
                    self.rayo.xy
                ],
                "Direction": [
                    self.rayo.vector
                ],
                "Times": [
                    self.rayo.time
                ]
            }
        )

        self.data = pd.concat([self.data, temp], ignore_index=True)

        which_vector = np.all(self.border_vector == self.capa.top_vector)

        if (
            which_vector
        ):

            self.border_vector = self.capa.bottom_vector

        else:

            self.border_vector = self.capa.top_vector





    def run(self):

        while (self.rayo.continue_simulation):
            self.step()

        self.graph.setDataframe(self.data)
        print(self.graph.dataframe)
        self.graph.create(self.count)
        self.graph.show()
