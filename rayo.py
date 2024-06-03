import math
import operator

import numpy
import numpy as np

class Rayo:
    def __init__(self, xy, vector, capa):
        self.xy = xy
        self.vector = vector
        self.capa = capa
        self.magnitude = math.sqrt( (self.vector[1])**2 + (self.vector[0])**2 )
        self.slope = self.vector[1] / self.vector[0]
        self.b = self.xy[1] - self.slope * self.xy[0]
        self.continue_simulation = True



    def solve_for_t(self, border_vector):

        # <t> = A^-1 * <b>

        A = np.array(
            [
            [self.vector[0], -border_vector[0]],
            [self.vector[1], -border_vector[1]]
            ]
        )

        A_inv = np.linalg.inv(A)

        b = numpy.array(
            [
                self.xy[0] + self.capa.xy[0],
                self.xy[1] + self.capa.xy[1]
            ]
        )

        t = np.dot(A_inv, b)

        return t

    def get_xy(self, t):

        # x = x_0 + <v> * t
        # y = y_0 + <v> * t

        x = self.xy[0] + self.vector[0] * t
        y = self.xy[1] + self.vector[1] * t

        return numpy.array([x, y])

    def move(self, border_vector):

        # I need to check if the current direction will imply no intersection between rayo() and border

        result = (
            math.atan(self.vector[1] / self.vector[0]) < math.atan(self.capa.top_vector[1] / self.capa.top_vector[0]) or
            abs(math.atan(self.vector[1] / self.vector[0])) < abs(math.atan(self.capa.bottom_vector[1] / self.capa.bottom_vector[0]))
        )

        A = np.array([
            [self.vector[0], -border_vector[0]],
            [self.vector[1], -border_vector[1]]
        ])

        b = np.array([
            self.capa.xy[0] - self.xy[0],
            self.capa.xy[1] - self.xy[1]
        ])

        t = np.dot(np.linalg.inv(A), b)

        x = self.vector[0] * t[0] + self.xy[0]
        y = self.vector[1] * t[0] + self.xy[1]

        self.xy = np.array([x, y])


    def reflect(self, border_vector):

        # specular reflection
        # v_r = v_i - 2 * v_n * (v_n dot v_i)

        v_n = np.array([-border_vector[1], border_vector[0]]) / np.linalg.norm(border_vector)
        v_s = self.vector - 2 * v_n * (np.dot(self.vector, v_n))
        self.vector = v_s
        self.slope = self.vector[1] / self.vector[0]
        self.b = self.xy[1] - self.slope * self.xy[0]
        self.magnitude = math.sqrt((self.vector[1]) ** 2 + (self.vector[0]) ** 2)