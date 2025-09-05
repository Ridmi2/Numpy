import numpy

print (numpy.__version__)
x=numpy.array([1,3,5],ndmin=4)

print (x)
print(x.ndim)

y=numpy.array([[1,2,3],[4,5,6]])
print (y)

print(y.ndim)

z=numpy.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print (z)

print(z.ndim)