import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math
from scipy.stats import binom
prob=1-binom.cdf(56,100,0.5)
print(prob)

print(binom.ppf(0.95,100,0,5)+1)

mu = 50
variance = 10
sigma = math.sqrt(variance)
x = np.linspace(1, 100, 200)
plt.plot(x,stats.norm.pdf(x, mu, sigma))

mu = 60
variance = 10
sigma = math.sqrt(variance)
x = np.linspace(1, 100, 200)
plt.plot(x,stats.norm.pdf(x, mu, sigma))

plt.xlim(30,80)
plt.show()