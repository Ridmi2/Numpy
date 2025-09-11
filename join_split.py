import numpy as np 

arr1=np.array([1,3,2])
arr2=np.array([4,5,6])


newarr=np.concatenate((arr1,arr2))
print(newarr)


#two dimensional array
arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6],[7,8]])

newarr1=np.concatenate((arr3,arr4),axis=0)
print(newarr1)