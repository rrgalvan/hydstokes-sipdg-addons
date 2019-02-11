#!/usr/bin/python3

from numpy import *
from matplotlib.pylab import *
import os

order_names = ["u_H1", "u_L2", "v_L2", "p_L2"]
line_styles=["-","--","-.",":"]
line_markers=["o","s","^","+"]

orders={k:None for k in order_names}

print(orders)

for o in order_names:
    filename = o + "_errors.txt"
    with open(filename, 'r') as f:
        orders[o] = [float(x) for x in f.readlines()]

n = len(list(orders.values())[0])
h0 = sqrt(2)/8
x = [ h0/(n+1) for n in range(n) ]

for o,s,m in zip(order_names,line_styles,line_markers):
    y = orders[o]
    loglog(x,y,linestyle=s,label=o,marker=m)
legend()
show()
