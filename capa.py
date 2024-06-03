import numpy


class Capa:
    def __init__(self, xy, top_vector, bottom_vector):
        self.xy = xy
        self.top_vector = top_vector
        self.bottom_vector = bottom_vector
        self.top_slope = self.top_vector[1] / self.top_vector[0]
        self.top_y_intercept = self.xy[1] - self.top_slope * self.xy[0]
        self.bottom_slope = self.bottom_vector[1] / self.bottom_vector[0]
        self.bottom_y_intercept = self.xy[1] - self.bottom_slope * self.xy[0]

