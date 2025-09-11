import numpy as np
arr=np.array([[1,2],[3,4]])
arr1 =np.array([1,3,5,7])

x=np.searchsorted(arr1,[2,3,8])
print(x)
x=np.where(arr==3)
print(arr)
print (x)