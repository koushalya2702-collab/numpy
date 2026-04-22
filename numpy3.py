#NumPy Array Slicing
import numpy as np
arr=np.array([2,3,4,5,6,7])
print(arr[1:5])

#example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])


#example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

#Negative Slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

#step
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

#Slicing 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

#example
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1])

#example
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
