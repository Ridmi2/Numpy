import numpy as np

x=np.array([1,2,3,4,5,6,7])
print(x.dtype)

y=x.astype('f')  
print(y.dtype)     

y=np.array(['apple','banana','cherry'])
print(y.dtype)


