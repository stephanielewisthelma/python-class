import numpy as np

# arr = np.array([1,2,3,4,5])

# print(arr)
print(type (arr))

# arr = np.array((45))
print (arr)

arr = np.array ([[1,2,3] ,[4,5,6]])
print (arr)

arr = np.array ([[[1,2,3] ,[4,5,6], [7,8,9]]])
print (arr.ndim)


# arr = np.array([1,2,3],ndim=6)


fruits =np.array (["mango","apple","lemon","orange"])
print(fruits)

arr =np.array ([10,20,30,40])
newArr = arr.astype('i')
print(newArr)
print(newArr.dtype)

arr =np.array([[1,2,3], [4,5,6],[40,50,60]])
print(arr.shape)
print(arr.size)

print(arr[0,0])


print(np.random.rand(300,1))