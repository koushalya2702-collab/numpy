#aggregate functions
import numpy as np
arr=np.array([1,2,3,4])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))


#axis concept
import numpy as np
arr=np.array([[4,5,6,7],[8,9,4,3]])
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))


#mathematical function
import numpy as np
arr=np.array([1,2,3,4])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))

#broadcasting
import numpy as np
a=np.array([1,2,3,4])
b=2
print(a*b)

#matrix operation
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,a.T))


#Random Numbers in NumPy
from numpy import random
x=random.randint(100)
print(x)

#Generate Random Float
from numpy import random
x=random.rand()
print(x)