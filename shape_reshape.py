import numpy as np

arr =np.array([1,2,3,4,5,6,7,8])
print(arr)


new = arr.reshape(2,2,-1)#have to kw two dimensions 


print(new)


arr1=np.array([[1,2,3],[4,5,6]])
new1=arr.reshape(-1)#one dimension
print(new1)