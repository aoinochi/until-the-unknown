import matplotlib.pyplot as plt

x=0
y=1.0
dx=0.1

x_values=[]
y_values=[]

for i in range(50):
    x_values.append(x)
    y_values.append(y)

    y=y+(-y)*dx
    x=x+dx
    plt.plot(x_values,y_values)
    plt.pause(0.1)
plt.show()

print(len(x_values),len(y_values))