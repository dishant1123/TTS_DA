# slicing ,statistical function  , maths function    : 
import numpy as np 

# maths function  : addition , sub  , mul , div , modulas , 

"""
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

b= np.array([
    [12,13,14],
    [15,16,17],
    [18,19,20]
])

print(a)
print(b)
print(a+b)  # 1+12   2 +13  3 +14  
print(a-b)
print(a/b)
print(a*b)  #   its not  matrix multiplication : ele by  multiply  
print(a%b)  # remainder :  1 %10    10 % 3 =1  
"""
# sum  sort  min max  arg min  arg max : 

"""a=np.array([
    [1,2,3],
    [4,-5,6],
    [7,8,9]
])
print(a) 
print(np.sum(a))  # sum of  all element 
print("col wise sum : ",np.sum(a,axis=0))  # axis = 0 col wise 
print("row wise  sum : ",np.sum(a,axis=1))  # axis = 1 row wise 

print(np.min(a)) # 1
print(np.min(a,axis =0)) #1 2 3 
print(np.min(a,axis=1)) # 1 4 7 
print(np.argmin(a))   #  return  index 
print(np.argmin(a,axis =0)) 
print(np.argmin(a,axis=1))


print(np.max(a)) # 9
print(np.max(a,axis =0)) #7 8 9  
print(np.max(a,axis=1)) # 3 6 9

print(np.argmax(a))
print(np.argmax(a,axis =0))
print(np.argmax(a,axis=1))

print(np.sort(a))  # asc to desc 
print(np.sort(a,axis=0))  # asc to desc
print(np.sort(a,axis=1))  # asc to desc
"""

# matrix multiplication : matmul ,dot , @ 

"""a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b= np.array([
    [12,13,14],
    [15,16,17],
    [18,19,20]
])

print("matrix A : \n",a)
print("matrix B : \n",b)

print("matrix A * B : \n",a@b)  # matrix multiplication
print("matrix A * B : \n",np.matmul(a,b))  # matrix multiplication
print("matrix A * B : \n",np.dot(a,b))  # matrix multiplication
"""
# transpose :
"""
transpose = a.T
transpose = np.transpose(a)
print("transpose of matrix A : \n",transpose)
"""

# slicing  , fancy indexing : 

"""
a=np.array([12,45,67,89,23,44,56,78])
print(a)
print(a[1 :5])  # start 1 end 5 
print(a[ 1:]) 
print(a[-1])
print(a[2 :5 :2 ]) # start 2  end 5 step 2 
 
b= np.array([
    [12,13,14,233,67,89],
    [15,16,17,999,65,32],
    [18,19,20,77,45,56],
    [21,22,23,88,77,66]
])
print(b)
print(b[0])  # first  row  ,  second  col 
print(b[1:3])  # row slicing  : 1 index 3 end 
print(b[1:4,1:3])  # row  slicing  : 1 :4  col slicing : 1 :3
print(b[2:4, : : -1])

"""
# fancy  indexing :

"""b= np.array([
    [12,13,14,233,67,89],
    [15,16,17,999,65,32],
    [18,19,20,77,45,56],
    [21,22,23,88,77,66]
])

print(b[[1,2,3]])
print(b[[1,2],[2,3]])   # 1,2  ==> row index 1 row index ==>2 2 row  index : 3 
print(b[[0,3],[0,2]])
"""

# statistical function :means median std  var 

"""
a=np.array([12,45,67,89,23,44,56,78])  # 12 23 44 45 56 67 78 89

print(a)
print(np.mean(a))  # mean
print(np.median(a))
print(np.std(a))
print(np.var(a))
"""

b= np.array([
    [12,13,14,233,67,89],
    [15,16,17,999,65,32],
    [18,19,20,77,45,56],
    [21,22,23,88,77,66]
])

b[2:4,1:3] =0 
print(b)