import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1, 2, 100)
# Convex function y1
y1 = np.exp(x)
plt.figure(1)
plt.plot(x, y1)
plt.xlabel('$x$')
plt.ylabel('$e^x$')
plt.show()

# Concave function y2
y2 = -np.exp(x)
plt.figure(2)
plt.plot(x, y2)
plt.xlabel('$x$')
plt.ylabel('$-e^x$')
plt.show()