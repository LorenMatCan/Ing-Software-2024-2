import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.figure()
plt.plot(x,y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funcion seno')
plt.legend()
plt.show()