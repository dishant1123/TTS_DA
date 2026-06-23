import numpy as np 
# flattern  ravel  :  use  convert 1d array  . 

"""a=np.arange(1,10).reshape(3,3)

x =a.flatten()  # new   array 
x[2] =900 
print("flattern array  is : \n",x)
print("original array  is : \n",a)

a=np.arange(1,10).reshape(3,3)
x =a.ravel()  # # view ()   ===> memory shared
x[2] =900 
print("ravel array  is : \n",x)
print("original array  is : \n",a)

l1 =[1,2,3,4,5]
l2= l1.copy()  # l2 = [1,2,3,4,5]
l2.append(90)
print("l2 is : \n",l2)
print("l1 is : \n",l1)

l1 =[1,2,3,4,5]
l2=l1     # view ()   ===> memory shared 
l2.append(90)
print("l2 is : \n",l2)
print("l1 is : \n",l1)
"""
# vstack  hstack  :

"""
a=np.arange(1,10).reshape(3,3)
b=np.arange(11,20).reshape(3,3)

print("original matrix : \n",a)
print("original matrix : \n",b)
result1  =np.vstack((a,b))
result  =np.hstack((a,b))

print("hstack :\n",result)
print("vstack :\n",result1)
"""

# dstack  : convert  in to 3d array 
"""
a=np.arange(1,10).reshape(3,3)  # 2d 
b=np.arange(11,20).reshape(3,3)  # 2d 

result1  =np.dstack((a,b))
print("dstack :\n",result1)


[[1,2,3],   [[11,12,13],
[4,5,6],     [14,15,16],
[7,8,9]]     [17,18,19]]
"""
 

# concatenate  :

"""jan_sales =np.array([100,200,300,400,500])
feb_sales =np.array([10000,20000,30000,40000,50000])

concatenate = np.concatenate((jan_sales,feb_sales))
print("concatenate : \n",concatenate)
"""

# np.split  :

"""
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("arr : \n",arr)

result = np.split(arr,4)
print("result : \n",result)
"""
# np.array_split  :

"""
arr = np.array([1,2,3,4,5])
print("arr : \n",arr)

result = np.array_split(arr,4)
print("result : \n",result)
"""

# np.insert,append,remove , pop : 

"""
arr = np.array([1,2,3,4,5])
print(np.append(arr,6))
print(np.insert(arr,2,90))
arr[2] =34  # update  
print(arr)
print(np.delete(arr,2))  # index number wise  remove element 
"""

# utility function : unique , sort , argsort ,where ,nonzero 

arr = np.array([10,1,2,3,3,4,5])

# print(np.unique(arr))  # print unique element
# print(np.sort(arr))  # sort

# arr2 =np.array([40,30,10,20])
# print(np.argsort(arr2))

"""
40  30  10   20    ===> sort ===> 10   20   30   40 
0   1   2    3              ===>  2    3    1    0 
"""

"""marks = np.array([35,80,45,67,20])
result = np.where(marks >40,"pass","fail")
print(result)
"""

"""arr =np.array([12,45,67,0,34])
print(np.nonzero(arr))  # return  index of non zero element
"""

# np.all () ,np.any() ,np.isnan() :

arr =np.array([True,True,False,True])
# print(np.any(arr))  # check any element is true
# print(np.all(arr)) # check all element is true

# np.isinf () : 
"""arr = np.array([1,2,3,4,5,np.inf])
print(np.isinf(arr))  # is  ==> return  True  or  False

"""
# np.clip ()

sales = np.array([10000,12000,15000,17000,45000,75000])
print("sales : \n",sales)

print(np.clip(sales,10000,25000))

# IQR , z-score 