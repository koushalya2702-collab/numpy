#NumPy Creating Arrays
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

import numpy as np
arr=np.array((1,2,3))
print(arr)

#Dimensions in Arrays
#0-D Arrays
import numpy as np
arr=np.array(49)
print(arr)

#1-D Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#2-D Arrays
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D arrays
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

#Check Number of Dimensions
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b = np.array([1, 2, 3, 4, 5])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(d.ndim)

#Higher Dimensional Arrays
import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print('number of dimension :',arr.ndim)