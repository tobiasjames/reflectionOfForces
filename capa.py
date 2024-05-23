class Capa:
    def __init__(self, xy, vector1, vector2):
        self.xy = xy
        self.vector1 = vector1
        self.vector2 = vector2
        self.slope1 = self.vector1[1] / self.vector1[0]
        self.b1 = self.xy[1] - self.slope1 * self.xy[0]
        self.slope2 = self.vector2[1] / self.vector2[0]
        self.b2 = self.xy[1] - self.slope2 * self.xy[0]