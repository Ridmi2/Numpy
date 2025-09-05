import numpy as np 
x=np.array([1,2,3,4,5,6,7])
y=x.view()
z=x.copy()


print(y.base)
print(z.base)