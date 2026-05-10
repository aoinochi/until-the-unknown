import matplotlib.pyplot as plt
import numpy as np

x=0
v=1.0
t=0
dt=0.02
omega=2.0

x_values=[]
t_values=[]
v_values=[]

for i in range(1000):
    x_values.append(x)
    t_values.append(t)

    x=x+v*dt
    v=v+(-omega**2*x)*dt
    t=t+dt

for i in range(len(x_values)):
    plt.clf()

    plt.subplot(1, 2, 1)

    x_end = x_values[i]

    s = np.linspace(0, 1, 100)
    spring_x = s * x_end
    spring_y = 0.1 * np.sin(10 * np.pi * s)

    plt.plot(spring_x, spring_y)
    plt.scatter(x_end, 0, s=100)

    plt.xlim(-1, 1)
    plt.ylim(-0.5, 0.5)
    plt.title("Spring")

    plt.subplot(1, 2, 2)

    plt.plot(t_values[:i], x_values[:i]) 
    plt.scatter(t_values[i], x_values[i]) 

    plt.xlim(0, max(t_values))
    plt.ylim(-1, 1)
    plt.title("x(t)")

    plt.pause(0.01)

plt.show()