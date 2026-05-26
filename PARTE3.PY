import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import bisect

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

# ==========================
# BUSCAR CAMBIOS DE SIGNO
# ==========================

print("Cambios de signo:")

for i in range(len(V)-1):
    if V[i]*V[i+1] < 0:
        print(f"Entre {f[i]} y {f[i+1]} kHz")

# ==========================
# INTERPOLACION LINEAL
# ==========================

def interp_lineal(x,x0,y0,x1,y1):
    return y0 + (y1-y0)*(x-x0)/(x1-x0)

# ==========================
# FUNCIONES PARA BISECCION
# ==========================

def V1(x):
    return interp_lineal(x,55,0.012,57.5,-0.041)

def V2(x):
    return interp_lineal(x,62.5,-0.034,65,0.018)

# ==========================
# BISECCION
# ==========================

raiz1 = bisect(V1,55,57.5)
raiz2 = bisect(V2,62.5,65)

print("\nRaices por biseccion:")
print("Primera raiz =", raiz1,"kHz")
print("Segunda raiz =", raiz2,"kHz")

# ==========================
# SPLINE CUBICO
# ==========================

spline = CubicSpline(f,V,bc_type='natural')

raiz1_spline = bisect(spline,55,57.5)
raiz2_spline = bisect(spline,62.5,65)

print("\nRaices con spline:")
print("Primera raiz =", raiz1_spline,"kHz")
print("Segunda raiz =", raiz2_spline,"kHz")
