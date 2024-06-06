import math
import operator

import numpy
import numpy as np

class Rayo:
    def __init__(self, xy, vector, capa):
        self.xy = xy
        self.vector = vector
        self.capa = capa
        self.time = 0
        self.continue_simulation = True


    def move(self, border_vector):

        # I need to check if the current direction will imply no intersection between rayo() and border

        theta = math.atan((self.capa.top_vector[1]) / (self.capa.top_vector[0])) + -math.atan((self.capa.bottom_vector[1]) / (self.capa.bottom_vector[0]))

        test = math.atan(self.vector[1] / self.vector[0]) + -math.atan((self.capa.bottom_vector[1]) / (self.capa.bottom_vector[0]))

        if (test <= theta and test >= 0):

            self.continue_simulation = False

        else:

        # t = A^-1 * b

            A = np.array([
                [self.vector[0], -border_vector[0]],
                [self.vector[1], -border_vector[1]]
            ])

            b = np.array([
                self.capa.xy[0] - self.xy[0],
                self.capa.xy[1] - self.xy[1]
            ])

            t = np.dot(np.linalg.inv(A), b)

            # rayo(t_0) = (x,y)

            x = self.vector[0] * t[0] + self.xy[0]
            y = self.vector[1] * t[0] + self.xy[1]

            self.xy = np.array([x, y])
            self.time = t[0]

    def reflect(self, border_vector):

        # specular reflection
        # v_r = v_i - 2 * v_n * (v_n dot v_i)

        if (self.continue_simulation):

            v_n = np.array([-border_vector[1], border_vector[0]]) / np.linalg.norm(border_vector)
            v_s = self.vector - 2 * v_n * (np.dot(self.vector, v_n))
            self.vector = v_s