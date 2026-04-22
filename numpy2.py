#NumPy Array Indexing
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

#example
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])


#example
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


#Access 2-D Arrays
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,2])

#example
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr[1, 4])

#Access 3-D Arrays
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1,0,2])

#Negative Indexing
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-1])