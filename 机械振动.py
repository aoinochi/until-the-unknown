import matplotlib.pyplot as plt

x=0
v=1.0
t=0
dt=0.01
omega=2.0

x_values=[]
t_values=[]
v_values=[]

for i in range(1000):
    x_values.append(x)
    v_values.append(v)
    t_values.append(t)

    x=x+v*dt
    v=v+(-omega**2*x)*dt
    t=t+dt
         
plt.plot(t_values, x_values, label="x(t)")
plt.plot(t_values, v_values, label="v(t)")
plt.legend()
plt.show()