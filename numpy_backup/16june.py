"""
numpy  : array , matrix , vectorization , broadcasting 

list :  [1, ....100000]  ===> for loop  
numpy  : array  convert   ===> with few second 

inbuilt lib : random , datetime , math , statistics , 
pip install numpy 
"""
import numpy as np 

# np.array  : to create  array  
"""
a=np.array([1,23,45,67,89])
print(a)
print(type(a))

b= np.array([12,45.90,78,90],dtype=str)
print(b)
print(b.ndim)  # number of dimension
c= np.array([
    [1,2],
    [3,4]
])
print(c)
print(c.ndim)  # number of dimension

d= np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(d)
"""

# indexing  :  index start with 0   , index number ==> positive ==> l to r  negative ==> r to l
"""
a=np.array([1,23,45,67,89])
print(a)
print(a[3])
print(a[-1])   # last element 
print(a[-3])

# update : 
a[2] =43
print(a)
"""

# array attribute :

"""a=np.array([1,23,45,67,89])
print(a)
print(a.shape)   # row ,col 
print(a.ndim)  # number of dimension
print(a.size)  # total element
print(a.itemsize)  # size of each element
print(a.dtype)  # int 

c= np.array([
    [1,2],
    [3,4]
])
print(c.shape)
"""

# array  function : arange , zeros ,ones ,full ,eye ,size ,reshape 

# arr =np.arange(10)  # start , stop ,step   : if  start position  missing then  by default array start  from  0 
# arr =np.arange(1,10)
# arr =np.arange(1,10,3)  # 1 start  10 stop  2 step 
     # 1 4 7 

# arr=np.arange(1,10).reshape(3,3)
# print(arr)

import  random  as rd 

# arr= np.random.randint(low=-10,high=10,size=(4,3))
arr= np.random.randint(low=-10,high=10,size=12).reshape(12,1)
# print(arr)

arr1=np.random.random(size=10).reshape(5,2)  # 0-1 
# print(arr1)

arr2 = np.arange(1,33).reshape(2,2,2,4)    # 32 elements   # 2 2  2 row ,4 col 
# print(arr2)            

arr3 =np.ones((3,3),dtype=int)  # 3 row , 3 col
# print(arr3)

arr4 =np.zeros((3,3),dtype=int)  # 3 row , 3 col
# print(arr4)

arr5 =np.full((3,3),fill_value=100,dtype=int)  # 3 row , 3 col
# print(arr5)

# identity matrix :
"""
1 0 0  (0,0)1  (0,1)0  (0,2)0
0 1 0  (1,0)0  (1,1)1  (1,2)0
0 0 1  (2,0)0  (2,1)0  (2,2)1
0 0 1
"""
"""arr6 =np.eye(4,dtype=int)  # 3 row , 3 col
print(arr6)
"""

# linspace : 

arr7 = np.linspace(1,10,3)  # start :1  stop   10  step :3 
print(arr7)
# formula  : stop -start /step-1    : 10 -1 /3-1 = 9/2  =4.5
