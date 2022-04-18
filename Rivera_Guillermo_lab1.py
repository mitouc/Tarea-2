from sympy import Function, dsolve, Derivative, sin, cos, exp, checkodesol, symbols
from sympy.abc import x
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
y = Function("y")
print(dsolve(Derivative(y(x),x,x) -2* Derivative(y(x),x) + y(x) -x*exp(x) -sin(2*x), y(x)))
x,C1,C2 = symbols("x,C1,C2")
print(checkodesol(y(x).diff(x,2) - 2* y(x).diff(y(x)) + y(x) - x*exp(x) - sin(2*x), (C1 + x*(C2 + x**2/6))*exp(x) - 3*sin(2*x)/25 + 4*cos(2*x)/25 ))
def EDO(y,x,k):
    dydx = k*y*(501-y)
    return dydx 
y0 = 1
x = np.arange(0.0,5.0,0.1)
k = 0.003
y1 = odeint(EDO,y0,x,args=(k,))
k = 0.02
y2 = odeint(EDO,y0,x,args=(k,))
k = 0.1
y3 = odeint(EDO,y0,x,args=(k,))
plt.plot(x,y1,label="k=0.003",color="blue")
plt.plot(x,y2,label="k=0.02",color="black")
plt.plot(x,y3,label="k=0.1",color="red")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.show()
# El comportamiento de la cantidad de enfermos de la comunidad en base al
# valor de la constante k es claro, ya que a mayor valor de la constante k
#, mayor es la tasa de contagiados a medida del tiempo, como se puede ver
# en el grafico, siendo k = 0,1 el de mayor tasa de contagio, siendo muy
# distinta la curva al caso de k = 0,003, la cual es más prolongada