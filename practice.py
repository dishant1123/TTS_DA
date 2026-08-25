import numpy as np 

"""arr=np.array([23,56,78,90,67])
print(arr)
print(type(arr))

arr2 =np.array([12,45,78.90])
print(arr2)
print(type(arr2))
print(arr2.ndim)  # number of  dimension 

arr3= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr3)
print(arr3.ndim)
print(arr3.shape)

# arr3[2] =900
# arr3[0:2] =900
arr3[1:3,1:3] =800
print(arr3)
"""
# np.arange :

# arr=np.arange(1,10)  # start stop  step 
arr=np.arange(1,10).reshape(3,3)

print(arr)
print(arr.size)

