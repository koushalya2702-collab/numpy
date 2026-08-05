#NumPy Filter Array
import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]
print(newarr)


#Example
import numpy as np
arr=np.array([43,45,67,42])
filter_arr=[]
for num in arr:
    if num > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)

#example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []

for element in arr:

  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#Creating Filter Directly From Array
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)