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

arr= np.genfromtxt("numpy_backup\student_info.txt",delimiter=",",dtype=None,skip_header=1,filling_values=0)
print("arr : \n",arr)


