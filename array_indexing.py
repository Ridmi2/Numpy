import numpy as np

arr=np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0])

print(arr[0]+arr[2])


#two dimensional array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1[0,1])

#three dimensional array\
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
print(arr2[0,1,2])


#negative ibdexing
print(arr[-1])