import numpy as np
from rayo import Rayo
from capa import Capa
from sim import Sim

c1 = Capa(
    xy=np.array([-3, 0]),
    top_vector=np.array([1, 1]),
    bottom_vector=np.array([1, -0.5])
)

x = 1
M = lambda v : v[1] / v[0]
B = lambda xy, v : xy[1] - (v[1] / v[0]) * xy[0]
y = M(c1.bottom_vector) * x + B(c1.xy, c1.bottom_vector)     ########### y = mx + b

f1 = Rayo(
    xy=np.array([x, y]),
    vector=np.array([1, 1]),
    capa=c1
)

sim = Sim(capa=c1, rayo=f1)

sim.run(5)

print("done")