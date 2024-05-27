import numpy as np
from fuerza import Fuerza
from capa import Capa
from sim import Sim


c1 = Capa(xy=np.array([0, 0]), vector1=np.array([1, 0]), vector2=np.array([3, -2]))

x = 2
M = lambda v : v[1] / v[0]
B = lambda xy, v : xy[1] - (v[1] / v[0]) * xy[0]
y = M(c1.vector2) * x + B(c1.xy, c1.vector2)     ########### y = mx + b

f1 = Fuerza(xy=np.array([x, y]), vector=np.array([1, 2]))

sim = Sim(capa=c1, fuerza=f1)

sim.run(5)

print("done")