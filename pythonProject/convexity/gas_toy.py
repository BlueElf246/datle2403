import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import minimize
import seaborn as sns

# generate data
price = np.random.randint(1000,7000, size=1000)
volume = ((-price/2)+4000).astype('int')
cost = 300+volume*0.25
profit = (price - cost)*volume
df_pv = pd.DataFrame({'price':price,
                     'volume':volume,
                     'cost':cost,
                     'profit':profit})
df_pv= df_pv.sort_values(by='price').reset_index(drop=True)
# import plotly.graph_objects as go
# import numpy as np
# from plotly.offline import iplot
# # Read data
# z_data = df_pv[['price','volume','profit']]
#
# fig = go.Figure(data=[go.Mesh3d(x=(z_data['price'].values),
#                                y=(z_data['volume'].values),
#                                z=(z_data['profit'].values),
#                    opacity=0.5,
#                    color='rgba(244,30,20,0.6)'
#                   )])
# fig.update_layout(title='Price Volume - Profit Curve', autosize=True)
#
#
# iplot(fig)
import numpy as np
from scipy import optimize
import statsmodels.api as sm
df_pv_small=df_pv[df_pv['price']<3000]
df_pv_small.tail()
X= df_pv_small[['price']]
y=df_pv_small[['volume']]
X = sm.add_constant(X)

mod_vol = sm.OLS(y,X)
mod_vol = mod_vol.fit()
mod_vol.summary()