import numpy as np
from scipy.interpolate import CubicSpline

# ==========================
# DATOS
# ==========================

f = np.array([
10,12.5,15,17.5,20,22.5,25,27.5,30,32.5,
35,37.5,40,42.5,45,47.5,50,52.5,55,57.5,
60,62.5,65,67.5,70,72.5,75,77.5,80,82.5,
85,87.5,90,92.5,95,97.5,100,102.5,105,107.5
])

V = np.array([
0.842,0.911,0.986,1.062,1.143,1.227,1.314,1.401,
1.482,1.551,1.216,1.048,0.866,0.689,0.521,0.364,
0.223,0.103,0.012,-0.041,-0.057,-0.034,0.018,
0.096,0.197,0.318,0.452,0.579,0.700,0.809,
0.611,0.688,0.756,0.811,0.856,0.894,0.926,
0.954,0.980,1.004
])

h = 2.5

# ==========================
# DIFERENCIA CENTRADA ORDEN 2
# ==========================

def derivada_centrada_2(y_prev, y_next, h):
    return (y_next - y_prev)/(2*h)

# 40 kHz
d40_o2 = derivada_centrada_2(1.048,0.689,h)

# 70 kHz
d70_o2 = derivada_centrada_2(0.096,0.318,h)

# 100 kHz
d100_o2 = derivada_centrada_2(0.894,0.954,h)

print("Orden 2")
print("dV/df(40) =", d40_o2)
print("dV/df(70) =", d70_o2)
print("dV/df(100) =", d100_o2)

# ==========================
# DIFERENCIA CENTRADA ORDEN 4
# ==========================

def derivada_centrada_4(fm2, fm1, fp1, fp2, h):
    return (-fp2 + 8*fp1 - 8*fm1 + fm2)/(12*h)

d40_o4 = derivada_centrada_4(1.216,1.048,0.689,0.521,h)

d70_o4 = derivada_centrada_4(0.018,0.096,0.318,0.452,h)

d100_o4 = derivada_centrada_4(0.856,0.894,0.954,0.980,h)

print("\nOrden 4")
print("dV/df(40) =", d40_o4)
print("dV/df(70) =", d70_o4)
print("dV/df(100) =", d100_o4)

# ==========================
# DIFERENCIA PROGRESIVA ORDEN 2
# ==========================

d10_prog = (-3*0.842 + 4*0.911 - 0.986)/(2*h)

print("\nExtremo inferior")
print("dV/df(10) =", d10_prog)

# ==========================
# DERIVADA DEL SPLINE
# ==========================

spline = CubicSpline(f,V,bc_type='natural')

print("\nSpline cúbico")
print("dV/df(40) =", spline.derivative()(40))
print("dV/df(70) =", spline.derivative()(70))
print("dV/df(100) =", spline.derivative()(100))
