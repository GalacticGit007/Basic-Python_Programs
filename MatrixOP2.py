import numpy as np
#inverse of Matrix
A=np.array([[1,2,5],[6,4,8],[6,7,9]])
print("The matrix is A =\n",A)
print("The inverse of matrix A =\n",np.linalg.inv(A))

#Eigen values
eigval,eigvec=np.linalg.eig(A)
print("Eigen value =",eigval)
print("Eigen Vector :\n",eigvec)

#Rank of a matrix
my_ar=np.arange(12).reshape(4,3)
rank=np.linalg.matrix_rank(my_ar)
print("Rank of the given Matrix is :",rank)
#K=np.array([0])