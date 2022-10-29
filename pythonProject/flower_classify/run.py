import h5py
import numpy as np
import pandas as pd
from  imutils import  paths
import cv2
data=[]
path='flower_images/flower_images/'
imagepath=list(paths.list_images('flower_images/flower_images/'))
for image in imagepath:
    f=cv2.imread(image)
    data.append(f)
print(len(data))
np_array=np.array(data)
np_array.reshape(210,1)





