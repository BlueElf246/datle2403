import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import matplotlib.image as mplib
from sklearn.decomposition import PCA
import pandas as pd
import imageio
img_r = mplib.imread('data/subject01.centerlight')
print(img_r.shape)
plt.imshow(img_r)
pca = PCA(32)
img_transformed = pca.fit_transform(img_r)
print(img_transformed.shape)
print(np.sum(pca.explained_variance_ratio_) )
#var = pca.explained_variance_ratio_pca.components_[0]
z =img_transformed[:,2]
new_df = pd.DataFrame(z)
print(new_df.shape)