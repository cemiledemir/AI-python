import numpy as np #shortcut np
array = np.array([1,2,3,4]) #1*4 vector

print(array.shape)

a = array.reshape(2,2) # reshape array as an 2*2 new matris
print("shape: ",a.shape)
print("dimension: ",a.ndim)
print("size: ",a.size)
print("datatype: ",a.dtype)

print("type: ",type(a))

array1 = np.array([[1,2,3,3],[2,7,8,9],[3,4,5,6]]) 
np.zeros((5,6)) 

zeros = np.zeros((5,6)) 
zeros[3,4] = 5 make the 3rd row and 4th column  element 5 
print(zeros)

np.ones((3,4))
np.empty((4,6))

a = np.arange(10,50,5) #array([10, 15, 20, 25, 30, 35, 40, 45])
a = np.linspace(10,50,11) #array([10., 14., 18., 22., 26., 30., 34., 38., 42., 46., 50.])

#%%  numpy basic operations
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)
print(a**b)

print(np.sin(a))
degree = np.array([90,180,270]) #not angle
print(np.sin(degree))

print(a<2)

a = np.array([[1,2,3],[4,5,6]]) #a = np.array([1,2,3],[4,5,6])  TypeError: data type not understood
b = np.array([[4,5,6],[1,2,3]])
print(a*b)
a.dot(b) #Matrices a and b are not suitable for multiplying
b.T #transpose b
a.dot(b.T)

print(np.exp(a))
rand = np.random.random((3,4))
print(rand.sum())
print(rand.min())
print(rand.max())

print(rand.sum(axis=0)) #sum of columns
print(rand.sum(axis=1)) #sum of rows
#hata  print(rand.sum(axis=2)) axis=2 3. bir dimensioni belirtir ama yok   
print(np.sqrt(a)) #square root
print(np.square(a)) #a**2

print(np.add(a,b)) #a+b

# %% indexing and slicing

array = np.array([1,2,3,4,5,6])
print(array[3])
print(array[0:3])
reverse_array = array[::-1] #array([6, 5, 4, 3, 2, 1])
reverse_array = array[::-3] #array([6, 3])

a = np.array([[1,2,3],[4,5,6]])
print(a[0,2])
print(a[:,0:2])
print(a[1,1:3])

b = np.array([[4,5,6],[1,2,3],[3,6,7]])
print(b[-1,:])
print(b[-2,-3])

#shape maniuplation
array = np.array([[1,2,3],[4,5,6],[4,7,8]])
#flatten method
a = array.ravel() #array([1, 2, 3, 4, 5, 6, 4, 7, 8])
array2 = a.reshape(3,3)
array2.T

ar = np.array([[1,2],[3,4],[5,6]])
ar.reshape(2,3) 
ar.resize(2,3)

# %% array stacking

ar1 = np.array([[1,2],[3,4],[5,6]])
ar2 = np.array([[-1,-2],[-3,-4],[-5,-6]])

ar3 = np.vstack((ar1,ar2))
#vertical stack array([[ 1,  2],
                    # [ 3,  4],
                    #[ 5,  6],
                   # [-1, -2],
                    #[-3, -4],
                    #[-5, -6]])
ar6 = np.row_stack((ar1,ar2)) #vertical

ar4 = np.hstack((ar1,ar2))                
#horizontal stack array([[ 1,  2, -1, -2],
                     #   [ 3,  4, -3, -4],
                      #  [ 5,  6, -5, -6]])
ar5 = np.column_stack((ar1,ar2))  #(horizontal)   

# %% convert and copy arrays
liste = [1,2,3,4]
array = np.array(liste) #list convert to array

liste2 = list(array) #array covert to list
a = np.array([1,2,3])
b = a
c = a

b[0] = 5 #Changing the first value of b also changes the a and c arrays because this array is stored as a field, not a value in memory.
print(a)         #
#solution;
d = np.array([1,2,3])
e = d.copy() #with copy, a separate space is allocated  in memory for all of them. 
f = d.copy()

f[0] = 5 #f =array([5, 2, 3]) ancak  d =array([1, 2, 3]) e= array([1, 2, 3]) olur
