#realisation of two dimensional arrays and matrices and their visualization

import numpy as np 
import matplotlib.pyplot as plt

new_arr=np.array([[0.9,0.3],[0.8,0.6]])
print("The matrix is \n",new_arr)
plt.matshow(new_arr)

nxt_arr=np.array([[0.3,0.5,0.8],[0.1,0.2,0.9]])
plt.matshow(nxt_arr)
plt.show