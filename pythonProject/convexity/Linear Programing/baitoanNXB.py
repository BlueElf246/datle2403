# from cvxopt import matrix, solvers
# c=matrix([5.,10.,15.,4.])
# G=matrix([[1.,0.,1.,0.,-1.,0.,0.,0.], [0.,1.,1.,0.,0.,-1.,0.,0.], [1.,0.,0.,1.,0.,0.,-1.,0.], [0.,1.,0.,1.,0.,0.,0.,-1.]])
# h=matrix([600.,400.,800.,700.,0.,0.,0.,0.])
#
# solvers.options['show_progress'] = True
# sol = solvers.lp(c, G, h)
#
# print('Solution"')
# print(sol['x'])

import pandas as pd
df=pd.DataFrame([562, 869, 708, 775, 775, 704, 809, 856, 655, 806,

878, 909, 918, 558, 768, 870, 918, 940, 946, 661, 820, 898,

935, 952, 957, 693, 835, 905, 939, 955, 960, 498, 653, 730,

753])
print(df.describe())