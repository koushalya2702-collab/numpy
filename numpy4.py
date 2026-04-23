#NumPy Array Shape
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#example
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(arr.shape)

#example
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

#NumPy Array Reshaping
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr=arr.reshape(4,3)
print(new_arr)

#Reshape From 1-D to 3-D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
