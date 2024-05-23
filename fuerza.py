import math
import numpy as np

class Fuerza:
    def __init__(self, xy, vector):
        self.xy = xy
        self.vector = vector
        self.magnitude = math.sqrt( (self.vector[1])**2 + (self.vector[0])**2 )
        self.slope = self.vector[1] / self.vector[0]
        self.b = self.xy[1] - self.slope * self.xy[0]
        self.distance = None

    def move(self, border_vector, capa):

        # scale vector to distance to intersection

        # y-intercept form of border_vector
        m_1 = border_vector[1] / border_vector[0]
        b_1 = capa.xy[1] - (border_vector[1] / border_vector[0]) * capa.xy[0]

        # y-intercept form of self.vector
        m_2 = self.vector[1] / self.vector[0]
        b_2 = capa.xy[1] - (self.vector[1] / self.vector[0]) * capa.xy[0]

        # interception point of border_vector and self.vector
        x = (b_2 - b_1) / (m_1 - m_2)
        y = m_1 * x + b_1

        self.distance = math.sqrt( (x - self.xy[0])**2 + (y - self.xy[1])**2)

        norm = np.linalg.norm(self.vector)
        self.xy = np.add(self.xy, (self.distance / norm) * self.vector)

    def reflect(self, border_vector):

        # specular reflection
        # v_r = v_i - 2 * v_n * (v_n dot v_i)

        v_n = np.array([-border_vector[1], border_vector[0]]) / np.linalg.norm(border_vector)
        v_s = self.vector - 2 * v_n * (np.dot(v_n, self.vector))
        self.vector = v_s