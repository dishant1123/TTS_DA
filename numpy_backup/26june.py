import numpy as np

#loadtxt : use when dataset is  clean  no missing value  and only use when numreic data. 

"""arr= np.loadtxt("numpy_backup\student_marks.txt",delimiter="\t",dtype=int)
print("arr : \n",arr)

print(arr.shape)
print(arr.dtype)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.std())
print(arr.sum())
"""
# genfromtxt : handling missing value 

"""arr= np.genfromtxt("numpy_backup\student_info.txt",delimiter=",",dtype=None,skip_header=1,filling_values=0)
print("arr : \n",arr)

"""

# broardcast : 

# case 1:
"""
a=np.array([1,2,3,4,5,6])   # shape : 1d  ===> 6, 
b= np.array([23,45,67,89,10,34]).reshape(2,3)  # shape : 2d  ===> 2,3

print("a : \n",a)
print("b : \n",b)
print("a+b : \n",a+b)
"""
# case 2 : 
"""a=np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
b= np.array([[23,45,67,89,10,34]]).reshape(2,3)  # shape : 2d  ===> 2,3

print("a : \n",a)  # shape : 6,1`
print("b : \n",b)  # shape : 2,3

print("a+b : \n",a+b)
"""

# case 3 : 

"""
a=np.array([
    [1,2,3], 
    [4,5,6]
])
b=np.array([10,20,30])

print("a : \n",a)
print("b : \n",b)

print("a+b : \n",a+b)
"""
# case 4 : 

a=np.array([
    [1,2,3], 
    [4,5,6]
])
b=np.array([[10],
            [20]])
print(a+b)

