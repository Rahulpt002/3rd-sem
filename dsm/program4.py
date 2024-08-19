#matrix Operation
import numpy as np
print("Matrix Operation")
a=np.array([[2,4],[6,3]])
b=np.array([[1,2],[3,5]])
c=a+b
d=a-b
e=a*b
f=np.dot(a,b)
a_transpose=a.T
print("\nMatrix A:\n",a)
print("\nMatrix B:\n",b)
print("\nAddition:\n",c)
print("\nSubstraction:\n",d)
print("\nMultiplication (Element-wise):\n",e)
print("\nMultiplication (Row x Column):\n",f)
print("\nTranspose:\n",a_transpose)


#with SVD

import numpy as np
#create a sample matrix
X=np.array([[1,2,3],[4,5,6],[7,8,9]])

#perform SVD
U,S,VT=np.linalg.svd(X)

#choose the number of components to keep(eg:2)
n_components=2

#Reconstruct the matrix with reduced dimensions
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix:")
print(X)
print("\nReconsructed Matrix(with reduced dimensions):")
print(X_reconstructed)
