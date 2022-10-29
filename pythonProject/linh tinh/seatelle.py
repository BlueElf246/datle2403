import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn; seaborn.set()
rainfall = pd.read_csv('../Example/Seattle2014.csv')['PRCP'].values
inches=rainfall/254
# inches.shape
# plt.hist(inches,40)
# plt.show()
Summer=(np.arange(365)-172 >90) & (np.arange(365)-172>0)
y=(np.arange(365)-172 >90) # True when reach 172nd number
rainy= inches >0
print(rainy)
print(inches[rainy & ~Summer]) # only show value which is True


