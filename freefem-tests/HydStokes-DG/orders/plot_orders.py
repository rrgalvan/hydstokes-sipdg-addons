#!/usr/bin/python3

from numpy import *
from matplotlib.pylab import *
import os

order_names = ["u_H1", "u_L2", "v_L2", "p_L2"]
orders={k:None for k in order_names}

print(orders)

for o in order_names:
    filename = o + "_errors.txt"
    with open(filename, 'r') as f:
        orders[o] = [float(x) for x in f.readlines()]

n = len(list(orders.values())[0])
x = arange(n)
for o in order_names:
    y = orders[o]
    loglog(x,y,label=o)
legend()
show()
