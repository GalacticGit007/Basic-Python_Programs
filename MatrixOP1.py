#Basic matrix operations using python
import numpy as np

A=np.array([[1,2],[6,4]])
B=np.array([[1,1],[2,2]])
print("A =",A)
print("B =",B)
#using add fn in numpy
print("The element wise addition of matrix is :")
print(np.add(A,B))
#using subtract fn in numpy
print("The element wise substraction of matrix is :")
print(np.subtract(A,B))
#using divide fn in numpy
print("The element wise divison of matrix is :")
print(np.divide(A,B))
#using multiply fn in numpy
print("The element wise multiplication of matrix is :")
print(np.multiply(A,B))
#using dot fn in numpy
print("The product of matrices is :")
print(np.dot(A,B))

print("The transpose of matrices A is :")
print(A.T)

detA=np.linalg.det(A)   # Calling det fn from linear algebra in numpy
print("The determinant is ",detA)

ID_mat=np.eye(3,3,dtype=int)
print("Identity matrix is :\n",ID_mat)

#Reshape Array

arr1= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
new_arr1 =arr1.reshape(8,2)
print("The reshaped array is :\n",new_arr1)

my_ar=np.arange(12).reshape(4,3)
#Swapping column
my_ar[:,[2,0]]= my_ar[:,[0,2]]
print(my_ar,"\n")
print("After swaping :\n")
print(my_ar)

my_ar2=np.arange(16).reshape(4,4)
#Swapping Row
print(my_ar2,"\n")
my_ar2[[0,2]]=my_ar2[[2,0]]
print("After  swaping :\n")
print(my_ar2)
