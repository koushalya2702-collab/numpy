#NumPy Data Types
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)


#Example
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

#Creating Arrays With a Defined Data Type
import numpy as np
arr=np.array([1,2,3,4],dtype='S')
print(arr)
print(arr.dtype)

#example
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#Converting Data Type on Existing Arrays
import numpy as np

arr = np.array([1.1, 2.1, 3.1])
new_arr=arr.astype('i')
print(new_arr)
print(type(new_arr))


#Example
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)